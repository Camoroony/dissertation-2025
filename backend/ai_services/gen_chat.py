from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def generate_chat(prompt: str, chat_history=None, workout_plan=None):

    response = generate_generic_chat(prompt, chat_history) if workout_plan is None else generate_workout_chat(prompt, chat_history, workout_plan)

    return response

def generate_generic_chat(user_prompt: str, chat_history):

    vectorstore = get_chroma_vectorstore(db_name="overall_db", db_data="*")

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=user_prompt, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    ai_context = (
    "\n\n You will be provided with some relevant documents and a chat history to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n USE ONLY THE DOCUMENTS AND/OR THE CHAT HISTORY PROVIDED TO FORMULATE YOUR ANSWER"
    + "\n These are the relevant documents you must use to formulate your answer:"
    + "\n **Relevant Documents:**"
    + f"\n{context_text}"
    + "\n **Chat History:**"
    + f"\n{chat_history['chats']}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot assistant who answers muscular hypertrophy and weightifting questions only.\n\n"),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer based on the documents: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": user_prompt})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(ai_response)

    return {
       "ai_response": ai_response,
       "sources": sources
    }


def generate_workout_chat(prompt: str, chat_history, workout_plan):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a chatbot who can answer questions about the following workout plan: {workout_plan}\n\n"
        "YOU ARE ONLY ALLOWED TO ANSWER QUESTIONS ABOUT THE WORKOUT PLAN.\n\n"
        "You have the following chat history with the user: {chat_history}. \n\n"),
        ("human", "This is the question for you to answer: {prompt}")

    ])

    formatted_input = {
        "workout_plan": workout_plan,
        "chat_history": chat_history,
        "prompt": prompt 
    }

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(formatted_input)

    return response


# Chat history BaseMessage formatting

def format_chat_history(chat_history):
    messages = []

    sys_message = SystemMessage(content=chat_history["sys_message"])

    messages.append(sys_message)

    for chat in chat_history["chats"]:
        messages.append(HumanMessage(chat["user_message"]))
        messages.append(AIMessage(chat["ai_message"]))

    return messages