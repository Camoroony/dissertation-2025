from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

def chatbot_answer_tool(ai_query: str):

    vectorstore = get_chroma_vectorstore(db_name="overall_db", db_data="*")
    vs_results = vectorstore.similarity_search_with_relevance_scores(query=ai_query, k=3)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    ai_context = (
    "\n\n You will be provided with a question that you must answer."
    "\n Documents have been provided that may assist you in your response."
    + "\n YOU MUST ONLY ANSWER THE QUESTION BASED ON THE PROVIDED DOCUMENTS."
    + "\n IF YOU CANNOT ANSWER THE QUESTION, STATE THAT YOU CANNOT ANSWER IT AND WHY."
    + f"\nHere are the following documents for you to use: {context_text}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who provides answers to questions regarding musclular hypertrophy and weightlifting."),
    ("system", "{ai_context}"),  
    ("human", "This is your task: {ai_query}")  
    ])

    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": ai_query})  

    return {
       "ai_response": ai_response,
       "sources": sources
    }


