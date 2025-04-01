from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_FUNCTION_SCHEMA
from models.db_models import WorkoutPlan
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY).with_structured_output(schema=WORKOUT_PLAN_FUNCTION_SCHEMA)

def build_workout_plan(workout_input: WorkoutGenInput, context):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a workout generator who generates workout plans for an individual."),

        ("system", "You will be provided context on the individual and recommendations to take into account for generating the workout plan. "
                   + "Use these recommendations to generate the workout plan with the individuals characteristics in mind."),     

        ("human", "Generate me a **hypertrophy workout plan** for an individual with the following context:\n"
                  + "- **Training Availability**: {training_availability} days per week\n\n"
                  + "- **Experience Level**: {experience_level}\n\n"
                  + "- **Session Length**: {session_length} minutes per session\n\n"
                  + "- **Training Focus**: {training_focus}\n\n"
                  + "- **Available Equipment**: {available_equipment}\n\n"
                  + "- **Additional Info**: {additional_info}"),
    ])

   
    formatted_input = {
        "training_availability": context["training_availability_context"],
        "experience_level": context["training_experience_context"],
        "session_length": workout_input.session_length,
        "training_focus": workout_input.training_focus,
        "available_equipment": context["training_equipment_context"],
        "additional_info": workout_input.additional_info if workout_input.additional_info else "None",
    }

    final_prompt = prompt_template.format(**formatted_input)

    
    chain = prompt_template | model

    
    response = chain.invoke(formatted_input)

    return {
        "context": final_prompt,
        "response": response
    }

