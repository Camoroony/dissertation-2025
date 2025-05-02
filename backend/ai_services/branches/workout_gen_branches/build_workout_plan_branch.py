from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_FUNCTION_SCHEMA
from security.openai_api_key import get_openai_api_key

OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY).with_structured_output(schema=WORKOUT_PLAN_FUNCTION_SCHEMA)

def build_workout_plan_ai(workout_input: WorkoutGenInput, context):

    prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert workout planner specialized in designing hypertrophy-focused training programs for individuals based on specific guidelines."),

    ("system", 
     "You will be provided with detailed parameters about the individual's workout structure, weekly set and exercise targets, available exercises, and other recommendations.\n"
     "Your job is to design a weekly hypertrophy workout plan that:\n"
     "- Follows the workout split structure.\n"
     "- Meets the required number of sets AND exercises per muscle group across the week.\n"
     "- Selects exercises only from the list provided.\n"
     "- Maintains a balanced distribution across muscle groups.\n"
     "- Honors the RIR guidance for intensity control.\n"
     "- Incorporates any additional user-specific notes."),

    ("human", 
     "**Generate a hypertrophy workout plan** based on the following individual-specific parameters:\n\n"
     "**1. Workout Split:**\n"
     "The structure below defines how many sessions to include in the week and what split type to use, including rationale:\n"
     "{workout_split}\n\n"

     "**2. Sets and Exercises per Muscle Group:**\n"
     "THE FOLLOWING STRUCTURE SHOWS THE NUMBER OF SETS AND EXERCISES YOU MUST PROGRAM INTO THE WORKOUT PLAN PER MUSCLE GROUP ACROSS THE WHOLE WEEK:\n"
     "{workout_sets}\n\n"

     "**3. Available Exercises:**\n"
     "Below is a list of exercises categorized by muscle group. ONLY select from these exercises when building the plan.\n"
     "Use as many exercises as needed to fulfill the set and exercise targets per muscle group, but DO NOT include more than what is required.\n"
     "{workout_exercises}\n"
     "USE A BALANCED NUMBER OF EXERCISES PER MUSCLE GROUP UNLESS OTHERWISE SPECIFIED. DO NOT EXCEED THE PROVIDED WEEKLY SET VOLUME FOR ANY GROUP.\n\n"

     "**4. Reps In Reserve (RIR):**\n"
     "Use the following RIR guidance to assign appropriate effort for each set: {workout_exercise_rir}\n\n"

     "**5. Additional Notes:**\n"
     "{additional_info}\n\n"
     
    )])


   
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

