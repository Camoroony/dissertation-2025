from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from database.chroma.init_chroma_db import build_chroma_vectorstore
from dotenv import load_dotenv
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini")

def get_available_equipment_context(available_equipment: str):

    vectorstore = build_chroma_vectorstore(db_name="available_equipment_db", db_data="available_equipment_studies")


    # print("\n--- Relevant Documents ---")
    # for i, doc in enumerate(relevant_docs, 1):
    #  print(f"Document {i}:\n{doc.page_content}\n")

    ai_query = f""
    context = ()

    prompt = ChatPromptTemplate.from_messages()

    chain = prompt | model | StrOutputParser()

    response = chain.invoke({"context": context, "ai_query": ai_query})  

    # print("\n--- Generated Response: ---")
    # print("Content:")
    # print(response.content)

    return response