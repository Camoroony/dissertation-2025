import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from database.chroma.init_chroma_db import get_chroma_vectorstore

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini")

def get_availability_context(training_availability: int):

    vectorstore = get_chroma_vectorstore(db_name="training_availability_db", db_data="training_availability_studies")

    retriever = vectorstore.as_retriever(search_type= "similarity_score_threshold",
                                     search_kwargs={"k": 6, "score_threshold": 0.4})

    vector_query = f"{training_availability} day workout split"

    relevant_docs = retriever.invoke(vector_query)

    # print("\n--- Relevant Documents ---")
    # for i, doc in enumerate(relevant_docs, 1):
    #  print(f"Document {i}:\n{doc.page_content}\n")

    ai_query = f"The individual wants to train {training_availability} days per week, suggest them the best workout split for {training_availability} sessions a week"

    context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n\n Some documents contain references to other sources by numbers e.g. [1], [2] etc. These numbers correspond with references that are marked with the same numbers at the end of documents e.g. [2] Example university (year), Paper title etc.."
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n DO NOT GIVE SAMPLE EXAMPLES OF A WORKOUT PLAN, YOU ARE ONLY TO RECOMMEND THE SPLIT TO FOLLOW AND EXPLAIN WHY"
    + "\n\n These are the relevant documents you must use to forumulate your answer:"
    + "\n\n Relevant Documents: \n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who provides concise advice on what workout split an individual should choose based on their characteristics."),
    ("system", "{context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    response = chain.invoke({"context": context, "ai_query": ai_query})  

    # print("\n--- Generated Response: ---")
    # print("Content:")
    # print(response.content)

    return response