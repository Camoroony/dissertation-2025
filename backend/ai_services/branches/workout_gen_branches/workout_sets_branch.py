from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from models.ai_models import MUSCLE_GROUP_SETS_SCHEMA, INDIVIDUAL_MUSCLES
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore
from security.openai_api_key import get_openai_api_key

OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


sets_model = model.with_structured_output(schema=MUSCLE_GROUP_SETS_SCHEMA)


def get_workout_sets_ai(training_experience: str, training_focus: str):

    workout_experience_chain = RunnableLambda(
        lambda _: get_workout_experience_sets(training_experience))
    
    workout_focus_chain = RunnableLambda(
        lambda x: get_workout_focus_sets(x, training_focus))

    full_chain = workout_experience_chain | workout_focus_chain

    chain_response = full_chain.invoke({})

    return {
       "ai_response": chain_response["ai_response"],
       "sources": chain_response["sources"]
    }
    


def get_workout_experience_sets(training_experience: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_sets_studies_vs", db_data="workout_sets_studies")

    vs_query = f"How many sets per muscle group per week should a {training_experience} weightlifter aim for?"

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    print(context_text)

    ai_query = (
    f"The individual is a {training_experience} weightlifter"
    + f"\nProvide an output of the amount of sets per week the individual should do for the following muscle groups, using the provided documents as evidence to determine your answer."
    + f"\nThese are the following muscle groups: {INDIVIDUAL_MUSCLES}"
    )

    ai_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT GIVE RECOMMEND WORKOUT SPLITS OR PLANS, YOU ARE ONLY TO RECOMMEND THE SETS PER WEEK TO DO FOR EACH MAJOR MUSCLE"
    + "\n\n These are the relevant documents you must use to formulate your answer:"
    + "\n\n Relevant Documents: \n\n"
    + f"{context_text}\n\n"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant for a workout generator who provides an output of the amount of sets per week an individual should do for each mucle depending on their personal characteristics.\n\n"),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | sets_model

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(ai_response)

    return {
       "ai_response": ai_response,
       "sources": sources
    }



def get_workout_focus_sets(experience_response: dict, training_focus: str):

    if training_focus == "Full-Body":
        return experience_response
    else:   

     vectorstore = get_chroma_vectorstore(db_name="workout_sets_studies_vs", db_data="workout_sets_studies")

     vs_query = f"How to develop muscles that are not responding as well as others?"

     vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=2)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"] | experience_response["sources"]

    print(context_text)

    ai_query = (
    f"The individual is looking to put more focus on growing their {training_focus} in their workout plan."
    + f"\nUsing the provided documents for your reasoning, reorganise the current sets for the workout plan to put more emphasis on the muscle the individual desires to prioritise."
    + "\nDO NOT ADD OR DELETE ANY SETS FROM THE TOTAL SET COUNT OF THE PLAN, YOU ARE ONLY REORGANISING THE SETS BASED ON THE DESIRED FOCUS FROM THE INDIVIDUAL."
    + f"\nThis is the current plan for you to alter based on the users focus desire:\n {experience_response['ai_response']}"
    )

    ai_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT PROVIDE OR RECOMMEND WORKOUT SPLITS OR PLANS, YOU ARE ONLY TO REORGANISE THE SETS OF A WORKOUT PLAN TO BETTER PRIORITISE THE DESIRED MUSCLE THE INDIVIDUAL WISHES TO FOCUS ON MORE."
    + "\n\n These are the relevant documents you must use to formulate your answer:"
    + "\n\n Relevant Documents: \n\n"
    + f"{context_text}\n\n"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant for a workout generator who reorganises the sets of a workout plan to have more emphasis on the muscle an individual wants"
    " to prioritise more.\n\n"),
    ("system", "{ai_context}\n\n"),  
    ("human", "This is your question to answer based on the documents:\n {ai_query}")  
    ])


    chain = prompt | sets_model

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(ai_response)

    return {
       "ai_response": ai_response,
       "sources": sources
    }