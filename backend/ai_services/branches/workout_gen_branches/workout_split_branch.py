from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def get_workout_split_ai(training_availability: int):

    vectorstore = get_chroma_vectorstore(db_name="workout_split_studies_vs", db_data="workout_split_studies")

    vs_query = f"What {training_availability} day workout splits are there?"

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=7)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    print(context_text)

    ai_query = (
    f"The individual wants to train {training_availability} days per week\n"
    + "Provide a brief 1 to 2 line summary of the individual and their desires, "
    + f"then suggest the individual the best workout split for {training_availability} sessions a week and state how many sessions a week it needs to be."
    )

    ai_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT GIVE SAMPLE EXAMPLES OF A WORKOUT PLAN, YOU ARE ONLY TO RECOMMEND THE SPLIT TO FOLLOW AND EXPLAIN WHY"
    + "\n\n These are the relevant documents you must use to formulate your answer:"
    + "\n\n Relevant Documents: \n\n"
    + f"\n\n {context_text}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who provides a description on an individuals workout split desires as well as advice on what workout split the individual should choose based on their characteristics."),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("\n\nContent:")
    print("\n" + ai_response)
    print("\n\nSources used:\n")
    print(sources)

    return {
       "ai_response": ai_response,
       "sources": sources
    }