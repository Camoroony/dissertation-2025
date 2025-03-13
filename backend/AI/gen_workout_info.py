from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from models.input_models import WorkoutGenInput
from models.ai_models import WORKOUT_PLAN_SCHEMA
from dotenv import load_dotenv
import os 


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_workoutsession_overview():
    
    return "Getting workout session overview!"



def generate_exercise_overview():

    return "Getting exercise overview!"
