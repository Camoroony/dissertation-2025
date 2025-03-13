from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_SCHEMA
from dotenv import load_dotenv
import os 


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)


def get_workoutsession_overview():
    
    return "Generating workout session overview!"


def generate_exercise_overview(context: str, exercise_id: int):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", f"You are a muscular hypertrophy workout assistant who has generated a workout based on the following context: {context}"),


        ("human", f"Give me an explanation of the exercise with the Id: {exercise_id}.\n"
         "Link the best youtube video on how to do the exercise at the end of the explanation.\n"
         "Explain the exercise and how to do it using references from academic paperas and provide the references in your explanation and at the end.\n")
    ])

    final_prompt = prompt_template.format()

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(final_prompt)
    
    return response
