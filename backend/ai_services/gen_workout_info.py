from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from typing import Dict, Any
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def generate_workoutsession_overview(context: str, workoutsession_id: int):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a muscular hypertrophy workout assistant who has generated a workout based on the following context: {context}\n."
                   "Your job is to provide explanations for why you generated the given workout session, explain how to do it, providing references and a youtube video tutorial for justification"
         
         ),


        ("human", "Give me an explanation of the session with the Id: {workoutsession_id}.\n"
         "Link the best youtube video on how to do the exercise at the end of the explanation.\n"
         "Explain the exercise and how to do it using references from academic papers, and provide the references in your explanation and at the end.\n")
    ])

    formatted_input = {
        "context": context,
        "workoutsession_id": workoutsession_id
    }

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(formatted_input)
    
    return response


def generate_exercise_overview(exercise: Dict[str, Any]):

    exercise_tutorial_runnable = RunnableLambda(
     lambda _: get_exercise_tutorial_ai(exercise["exercise_name"]))
    
    exercise_video_runnable = RunnableLambda(
     lambda x: get_exercise_video_ai(exercise["exercise_name"]))
    
    context_chain = RunnableParallel(
        exercise_tutorial_context = exercise_tutorial_runnable,
        exercise_video_context = exercise_video_runnable
    )

    final_generation = RunnableLambda(lambda x: build_exercise_overview_ai(x))


    final_chain = context_chain | final_generation

    response = final_chain.invoke({})
    
    return response
