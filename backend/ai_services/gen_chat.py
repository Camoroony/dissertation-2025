from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def generate_chat(prompt: str, chat_history=None, workout_plan=None):

    response = generate_generic_chat(prompt, chat_history) if workout_plan is None else generate_workout_chat(prompt, chat_history, workout_plan)

    return response

def generate_generic_chat(prompt: str, chat_history):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a chatbot with the following chat history: {chat_history}"),
        ("human", "{prompt}")

    ])

    formatted_input = {
        "chat_history": chat_history,
        "prompt": prompt 
    }

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(formatted_input)

    return response

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