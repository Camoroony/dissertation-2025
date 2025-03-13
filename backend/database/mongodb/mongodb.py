from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

def get_mongodb_client():

  client = MongoClient(MONGODB_URL)

  db = client["hypertrophy_edu_db"]

  return db
