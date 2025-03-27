from langchain_openai import ChatOpenAI
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from models.ai_models import MUSCLE_GROUPS
from database.chroma.init_chroma_db import get_chroma_vectorstore
from dotenv import load_dotenv
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini")

def get_available_equipment_context(available_equipment: str):

    vectorstore = get_chroma_vectorstore(db_name="test_db", db_data="available_equipment_studies")

    vectorstore_response = []

    data = vectorstore._collection.count()

    # for muscle in MUSCLE_GROUPS:
    query = f"What are the best shoulder exercises?"
    results = vectorstore.similarity_search_with_relevance_scores(query=query, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score, in results])
    print(context_text)
    # vectorstore_response.extend([doc.page_content for doc in relevant_docs])

    # print("\n--- Relevant Documents ---")
    # for i, doc in enumerate(vectorstore_response, 1):
    #  print(f"Document {i}:\n{doc}\n")

    prompt_context = (
    "\n\n You will be provided with some relevant documents to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n\n ONLY USE THE DOCUMENTS PROVIDED TO YOU TO FORMULATE YOUR ANSWER"
    + "\n\n These are the relevant documents you must use to forumulate your answer:"
    + "\n\n Relevant Documents: \n"
    + "\n\n".join([doc.page_content for doc, _score in results])
    )

    ai_query = (
    "What exercises for the Shoulders do you recommend?." 
    + "Please provide a list and give a one line explanation for your recommendation"
    )

    prompt = ChatPromptTemplate.from_messages([   
    ("system", "You are an assistant who provides exercise recommendations."),
    ("system", "{prompt_context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")])

    chain = prompt | model | StrOutputParser()

    response = chain.invoke({"prompt_context": prompt_context, "ai_query": ai_query})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(response)

    # return response