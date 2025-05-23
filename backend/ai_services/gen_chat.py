from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from security.openai_api_key import get_openai_api_key
from models.utilities.context_formatting import format_context
from database.chroma.init_chroma_db import get_chroma_vectorstore

OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def generate_chat(prompt: str, chat_history, workout_plans, workout_plan=None,):

    chat_type = chat_history.get('chat_type')

    if chat_type == 'Workout' and workout_plan is None:
        raise ValueError("Workout chat requires a workout_plan.")

    if chat_type == 'Community' and workout_plans is None:
        raise ValueError("Community chat requires a list of workout_plans.")

    match chat_type:
        case 'General':
            return generate_generic_chat(prompt, chat_history)
        case 'Workout':
            return generate_workout_chat(prompt, chat_history, workout_plan)
        case 'Community':
            return generate_community_chat(prompt, chat_history, workout_plans)
        case _:
            raise ValueError(f"Unsupported chat type: {chat_history['chat_type']}")
        


def generate_generic_chat(user_prompt: str, chat_history):

    vectorstore = get_chroma_vectorstore(db_name="overall_vs", db_data="*")

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=user_prompt, k=5)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    ai_context = (
    "\n\n You will be provided with some relevant documents and a chat history to use when answering the question"
    + "\n Your job is to provide an answer based on the following documents."
    + "\n USE ONLY THE DOCUMENTS AND/OR THE CHAT HISTORY PROVIDED TO FORMULATE YOUR ANSWER"
    + "\n IF THE DOCUMENTS OR CHAT HISTORY DO NOT PROVIDE YOU WITH THE ANSWER TO THE QUESTION, RESPOND SAYING YOU DON'T KNOW THE ANSWER."
    + "\n When you use any information from a source or sources, make sure to refer to the source directly in your response in this format: "
    + " ' [Source: Title: source_title, Author: source_author, URL: source_url]' to give context to the user."
    + "\n These are the relevant documents you must use to formulate your answer:"
    + "\n **Relevant Documents:**"
    + f"\n{context_text}"
    + "\n **Chat History:**"
    + f"\n{chat_history['chats']}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot assistant who answers muscular hypertrophy and weightifting questions only.\n\n"),
    ("system", "If your answer to a question is based on a source or sources, incorporate the source(s) you used into your text response.\n\n"),
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

def generate_community_chat(user_prompt: str, chat_history, workout_plans_info):

    workout_plans_text = "\n\n".join(
    f"Workout Plan {wp['id']}:\n\n{wp}\n\n{'=' * 40}" for wp in workout_plans_info
    )

    ai_context = (
    "\n\n You will be provided with workout plan information from the application's community page including ratings annd comments, as well as a chat history to use when answering the question."
    + "\n Your job is to provide an answer to the question based on these documents."
    + "\n USE ONLY THE WORKOUT PLAN INFO AND/OR THE CHAT HISTORY PROVIDED TO FORMULATE YOUR ANSWER"
    + "\n YOU ARE ONLY ALLOWED TO ANSWER QUESTIONS REGARDING WORKOUT PLANS, IF THE QUESTION IS ABOUT SOMETHING ELSE, EXPLAIN THAT YOU CANNOT ANSWER THE QUESTION AND WHY."
    + "\n This is the the workout plan information from the community page and the chat history you must use to formulate your answer:"
    + "\n **Workout Plan Information From The Community Page Including Ratings And Comments:**"
    + f"{workout_plans_text}"
    + "\n **Chat History:**"
    + f"\n{chat_history['chats']}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot assistant for an application who provides informative suggestions and answers to questions regarding workout plan selection for optimal muscular hypertrophy purposes.\n\n"),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer based on the workout plan information and chat history: {ai_query}")  
    ])


    chain = prompt | model | StrOutputParser()

    ai_response = chain.invoke({"ai_context": ai_context, "ai_query": user_prompt})  

    print("\n--- Generated Response: ---")
    print("Content:")
    print(ai_response)

    return {
       "ai_response": ai_response
    }



def generate_workout_chat(user_prompt: str, chat_history, workout_plan: dict):

    vectorstore = get_chroma_vectorstore(db_name="overall_vs", db_data="*")

    vs_results = vectorstore.similarity_search_with_relevance_scores(query=user_prompt, k=6)

    context = format_context(vs_results)

    context_text = context["documents"]
    sources = context["sources"]

    ai_context = (
    "\n\n You will be provided with some relevant documents and a chat history to use when answering the question."
    "\n\n You will also be provided a workout plan that you answer must be in reference to."
    + "\n Your job is to provide an answer to the question based on the following documents."
    + "\n USE ONLY THE DOCUMENTS AND/OR THE CHAT HISTORY PROVIDED TO FORMULATE YOUR ANSWER."
    + "\n IF THE DOCUMENTS OR CHAT HISTORY DO NOT PROVIDE YOU WITH THE ANSWER TO THE QUESTION, RESPOND SAYING YOU DON'T KNOW THE ANSWER."
    + "\n REMINDER: THE ANSWER MUST BE IN REFERENCE TO THE WORKOUT PLAN PROVIDED."
    + "\n When you use any information from a source or sources, make sure to refer to the source directly in your response in this format: "
    + " ' [Source: source_title, source_author, source_url]' to give context to the user."
    + "\n These are the relevant documents, chat history and workout plan you must use to formulate your answer:"
    + "\n **Relevant Documents:**"
    + f"\n{context_text}"
    + "\n **Chat History:**"
    + f"\n{chat_history['chats']}"
    + "\n **Workout Plan:**"
    + f"\n{workout_plan}"
    )

    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot assistant who answers muscular hypertrophy and weightifting questions regarding a workout plan.\n"),
    ("system", "ALL QUESTIONS MUST BE ANSWERED IN REFERENCE TO THE PROVIDED WORKOUT PLAN. YOU CAN ONLY ANSWER QUESTIONS REGARDING THE WORKOUT PLAN.\n"),
    ("system", "{ai_context}"),  
    ("human", "This is your question to answer about the workout plan based on the chat history and documents provided: {ai_query}")  
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

