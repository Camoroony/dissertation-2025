from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os 


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)


def get_workoutsession_overview():
    
    return "Generating workout session overview!"


def generate_exercise_overview(context: str, exercise_id: int):

    prompt_template = ChatPromptTemplate.from_messages([

        ("system", "You are a muscular hypertrophy workout assistant who has generated a workout based on the following context: {context}\n."
                   "Your job is to provide explanations for why you generated the given exercise, explain how to do it, providing references and a youtube video tutorial for justification"
         
         ),


        ("human", "Give me an explanation of the exercise with the Id: {exercise_id}.\n"
         "Link the best youtube video on how to do the exercise at the end of the explanation.\n"
         "Explain the exercise and how to do it using references from academic papers, and provide the references in your explanation and at the end.\n")
    ])

    formatted_input = {
        "context": context,
        "exercise_id": exercise_id
    }

    final_prompt = prompt_template.format(**formatted_input)

    chain = prompt_template | model | StrOutputParser()

    response = chain.invoke(formatted_input)
    
    return response
