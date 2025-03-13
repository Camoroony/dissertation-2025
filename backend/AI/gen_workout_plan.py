from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_SCHEMA
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_workout_plan(workout_input: WorkoutGenInput):

    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

    # Create a prompt template
    prompt_template = ChatPromptTemplate.from_messages([

        ("system", f"You are a workout generator who generates workout plans following this schema:\n{WORKOUT_PLAN_SCHEMA}\n"),


        ("human", "Generate me a hypertrophy workout plan for an individual with the following details:\n"
                  "- Experience Level: {experience_level}\n"
                  "- Training Availability: {training_availability} days per week\n"
                  "- Session Length: {session_length} minutes per session\n"
                  "- Training Focus: {training_focus}\n"
                  "- Available Equipment: {available_equipment}\n"
                  "- Additional Info: {additional_info}")
    ])

    # Convert available equipment to a comma-separated string
    formatted_input = {
        "experience_level": workout_input.experience_level,
        "training_availability": workout_input.training_availability,
        "session_length": workout_input.session_length,
        "training_focus": workout_input.training_focus,
        "available_equipment": ", ".join(workout_input.available_equipment) if workout_input.available_equipment else "None",
        "additional_info": workout_input.additional_info if workout_input.additional_info else "None"
    }

    # Create the chain
    chain = prompt_template | model | StrOutputParser()

    # Invoke the chain with the formatted input
    response = chain.invoke(formatted_input)

    return response

