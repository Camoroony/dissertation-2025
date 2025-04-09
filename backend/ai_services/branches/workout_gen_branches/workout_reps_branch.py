from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def get_workout_rir_ai(training_experience: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_reps_db", db_data="workout_reps_studies")

    vs_query = f"How many reps in reserve should a {training_experience} weightlifter do for their exercise sets?"

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=1)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    print(context_text)

    ai_query = (
    f"The individual is a {training_experience} weightlifter"
    + "Provide a brief 1 to 2 line summary of the individual and what you are determining for them."
    + f"\nThen provide an suggestion of the amount of reps in reserve the individual should do for their exercise repetitions, using the provided documents as evidence to determine your answer."
    )

    ai_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT GIVE RECOMMEND WORKOUT SPLITS OR PLANS, YOU ARE ONLY TO RECOMMEND THE REPS IN RESERVE PER WEEK TO DO FOR THE INDIVIDUALS EXERCISES."
    + "\n\n These are the relevant documents you must use to formulate your answer:"
    + "\n\n Relevant Documents: \n\n"
    + f"{context_text}\n\n"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant for a workout generator who provides an output of the amount of reps in reserve an individual should do for their exercise repetitions based on their personal characteristics and presented relevant documents.\n\n"),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(ai_response)

    return {
       "ai_response": ai_response,
       "sources": sources
    }