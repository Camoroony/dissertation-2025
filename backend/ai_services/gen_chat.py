from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import create_react_agent, create_structured_chat_agent, Tool, AgentExecutor
from langchain.schema.output_parser import StrOutputParser
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from ai_services.tools.generic_chatbot_answer_tool import chatbot_answer_tool
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def generate_chat(prompt: str, chat_history=None, workout_plan=None):

    response = generate_generic_chat(prompt, chat_history) if workout_plan is None else generate_workout_chat(prompt, chat_history, workout_plan)

    return response

def generate_generic_chat(prompt: str, chat_history):

    vector_tool = Tool(
    name="VectorSearch",
    func=chatbot_answer_tool,
    description=(
    "Use this tool when answering any questions that require access to external knowledge, "
    "especially about muscle building, hypertrophy, fitness science, or workout plans. "
    "This tool searches a knowledge base and returns relevant documents. "
    "If unsure or the answer may not be accurate, use this tool to improve reliability."
    "When using this tool, always return the sources used along with the answer."
)    )

    agent_prompt = hub.pull("hwchase17/structured-chat-agent")
    
    chat_agent = create_structured_chat_agent(
        llm=model,
        tools=[vector_tool],
        prompt=agent_prompt
    )

    agent_executor = AgentExecutor(
    tools=[vector_tool],
    llm=model,
    agent=chat_agent,
    verbose=True,
    handle_parsing_errors=True,
    )

    formatted_chat_history = format_chat_history(chat_history)

    response = agent_executor.invoke({
        "input": prompt,
        "chat_history": formatted_chat_history
    })

    return response["output"]

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