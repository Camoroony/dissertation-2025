from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

client = MongoClient(MONGODB_URL)

db = client["hypertrophy_edu_db"]

def add_chat_history():

    return "Adding chat history!"

def get_chat_history():

    return "Getting chat history!"

def add_workout_context():

    return "Adding workout plan context"

def get_workout_context():

    return "Getting workout plan context"