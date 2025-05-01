from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from security.openai_api_key import get_openai_api_key
from ai_services.branches.workout_info_branches.get_exercise_tutorial_branch import get_exercise_tutorial_ai
from ai_services.branches.workout_info_branches.get_exercise_video_branch import get_exercise_video_ai

OPENAI_API_KEY = get_openai_api_key()

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def generate_workoutsession_overview(context: str, workout_plan: dict, workout_session: dict):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a muscular hypertrophy workout assistant who has generated a workout based on the following context: {context}.\n"
                   "This is the workout plan you generated: {workout_plan}"),

        ("human", "Provide an overview of this session in the workout plan: {workout_session}\n"
         "Give an overview of the full session providing explanations and justifications for the sessions exercises, rep ranges and other attributes based on the context.\n")
    ])

    formatted_input = {
        "context": context,
        "workout_plan": workout_plan,
        "workout_session": workout_session
    }

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(formatted_input)
    
    return response


def generate_exercise_overview(exercise: str):

    exercise_tutorial_runnable = RunnableLambda(
     lambda _: get_exercise_tutorial_ai(exercise))
    
    exercise_video_runnable = RunnableLambda(
     lambda x: get_exercise_video_ai(exercise))
    
    context_chain = RunnableParallel(
        exercise_tutorial_context = exercise_tutorial_runnable,
        exercise_video_context = exercise_video_runnable
    )


    response = context_chain.invoke({})
    
    return response
