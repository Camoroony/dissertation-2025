from pymongo import MongoClient, ASCENDING, DESCENDING
import os
import glob
import json
import bson
from bson import BSON
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client["hypertrophy_edu_mongodb"]

def is_mongo_seeded():
    return mongo_db["chat_histories"].count_documents({}) > 0 or mongo_db["workout_contexts"].count_documents({}) > 0

def load_bson_from_file(file_path):
    with open(file_path, "rb") as file:
        return bson.decode_all(file.read())


def seed_mongo():
    print("Seeding MongoDB from MongoDB backup...")

    dummy_data_folder = glob.glob(os.path.join(os.path.dirname(__file__), "mongodbdummydata"))

    for filename in os.listdir(dummy_data_folder[0]):
        file_path = os.path.join(dummy_data_folder[0], filename)

        if filename.endswith(".bson"):
            print(f"Processing BSON file {filename}...")

            data = load_bson_from_file(file_path)

            collection_name = os.path.splitext(filename)[0]

            if collection_name:
                collection = mongo_db[collection_name]
                collection.insert_many(data)
                print(f"Inserted {len(data)} documents into {collection_name} collection.")

    print("MongoDB dummy data seeding complete.")
