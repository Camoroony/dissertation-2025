import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from database.chroma.init_chroma_db import get_chroma_vectorstore

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def get_workout_sets_ai(training_experience: str, training_focus: str):

    vectorstore = get_chroma_vectorstore(db_name="workout_sets_db", db_data="workout_sets_studies")

    vs_query = f"How many sets per muscle group should you do as a {training_experience} weightlifter?"

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=vs_query, k=7)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score, in vs_results])

    print(context_text)

    ai_query = (
    f"The individual is a {training_experience} weightlifter\n"
    + "Provide a brief 1 to 2 line summary of the individual and their desires, "
    + f"then suggest the individual the best amount of sets to do per muscle group as a {training_experience} weightlifter."
    )

    context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT GIVE SAMPLE EXAMPLES OF A WORKOUT PLAN, YOU ARE ONLY TO RECOMMEND THE SETS PER WEEK TO DO AND EXPLAIN WHY"
    + "\n\n These are the relevant documents you must use to formulate your answer:"
    + "\n\n Relevant Documents: \n\n"
    + f"\n\n {context_text}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who provides a description on an individuals weightlifting experience as well as advice on how many sets they should do per week per muscle group based on their characteristics."),
    ("system", "{context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    response = chain.invoke({"context": context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(response)

    return response