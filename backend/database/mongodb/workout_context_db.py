from database.mongodb.init_mongodb_db import get_mongodb_client

db = get_mongodb_client()

workout_context_collection = db["workout_contexts"]

def add_workout_context(workout_plan_id: int, context: str):

    document = {
        "workout_plan_id": workout_plan_id, 
        "context": context
    }

    result = workout_context_collection.insert_one(document)

    if result.inserted_id:
        return {"status": "success", "inserted_id": str(result.inserted_id)}
    else:
        raise ValueError("Failed to insert document.")
    

def get_workout_context(workout_plan_id: int):

    document = workout_context_collection.find_one({"workout_plan_id": workout_plan_id})

    if document:
        return document["context"]
    else:
        raise ValueError("Document is empty or not found.")