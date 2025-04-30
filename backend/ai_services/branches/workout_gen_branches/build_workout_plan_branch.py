from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_FUNCTION_SCHEMA
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY).with_structured_output(schema=WORKOUT_PLAN_FUNCTION_SCHEMA)

def build_workout_plan_ai(workout_input: WorkoutGenInput, context):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a workout generator who generates workout plans for an individual."),

        ("system", "You will be provided context on the individual and recommendations to take into account for generating the workout plan. "
                   + "Use these recommendations to generate the workout plan with the individuals characteristics in mind."),     

        ("human", "Generate me a **hypertrophy workout plan** for an individual with the following context:\n"
                  + "- **Recommended workout split**: {workout_split}\n\n"
                  + "- **Recommended sets per muscle group**:\n"
                  + "The following structure shows the number of sets you must program into the workout plan per muscle group for the week.\n"
                  + "{workout_sets}\n\n"
                  + "- **Recommended Exercises**: {workout_exercises}\n\n"
                  + "- **Recommended Reps In Reserve (RIR) for exercise sets**: {workout_exercise_rir}\n\n"
                  + "- **Additional info from the user to consider**: {additional_info}\n\n")
    ])

   
    formatted_input = {
        "workout_split": context["training_availability_context"]["ai_response"],
        "workout_sets": context["training_experience_context"]["ai_response"],
        "workout_exercises": context["training_equipment_context"]["ai_response"],
        "workout_exercise_rir": context["training_reps_context"]["ai_response"],
        "additional_info": workout_input.additional_info,
    }

    final_prompt = prompt_template.format(**formatted_input)

    sources = context["training_availability_context"]["sources"] | context["training_experience_context"]["sources"] | context["training_equipment_context"]["sources"] | context["training_reps_context"]["sources"]
    
    chain = prompt_template | model

    
    response = chain.invoke(formatted_input)

    return {
        "context": final_prompt,
        "sources_used": sources,
        "response": response
    }

