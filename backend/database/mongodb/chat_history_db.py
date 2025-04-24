from bson import ObjectId
from database.mongodb.init_mongodb_db import get_mongodb_client
import datetime


db = get_mongodb_client()

chat_history_collection = db['chat_histories']


def create_chat_history(user_id: int, chat_type: str = "General",  workout_plan=None):
    if chat_type not in {"General", "Community", "Workout"}:
       raise ValueError("Invalid chat type. Must be 'General', 'Community', or 'Workout'.")


    chat_history_document = {
        "user_id": user_id,
        "chat_type": chat_type,
        "chat_start_time": datetime.datetime.now(datetime.UTC),
        "chats": []
    }

    if chat_type == "Workout" and workout_plan is not None:
        chat_history_document["workout_plan_id"] = workout_plan.id
        chat_history_document["workout_plan_name"] = workout_plan.plan_name


    result = chat_history_collection.insert_one(chat_history_document)
    new_chat_history = chat_history_collection.find_one({"_id": result.inserted_id})

    return new_chat_history


def add_chat_history(chat_history_id: str, user_message: str, ai_response_data: dict[str, any]):
    if chat_history_id is None:
      raise ValueError("chat_history_id is null. Must be provided.")
    
    chat_message = {
        "chat_message_id": str(ObjectId()),
        "user_message": user_message,
        "ai_message": ai_response_data['ai_response'],
        "timestamp": datetime.datetime.now(datetime.UTC)
    }

    sources = ai_response_data.get('sources')

    if sources:
        chat_message["sources_used"] = list(sources)

    result = chat_history_collection.update_one(
    {"_id": ObjectId(chat_history_id)},
    {
        "$push": {
            "chats": {
                "$each": [chat_message],
                "$slice": -10
            }
        }
    }
)
        
    return f"Chat message (Id: {result}) added to chat history (Id: {chat_history_id}) "


def get_chat_history(chat_history_id: str):

    chat_history = chat_history_collection.find_one(
        {"_id": ObjectId(chat_history_id)},
    )

    if not chat_history:
       raise ValueError(f"Chat history with Id: {chat_history_id} not found.")

    return chat_history


def get_chat_histories_by_userid(user_id: int):

    chat_histories = chat_history_collection.find({"user_id": user_id})

    if not chat_histories:
        raise ValueError(f"No chat histories were found for user: {user_id}.")

    return list(chat_histories)

def delete_chat_history(chat_history_id: int):

    state = False

    result = chat_history_collection.delete_one({"_id": ObjectId(chat_history_id)})

    if result.deleted_count > 0:
        state = True
    
    return state

def delete_chat_history_by_user(user_id: int):
       
    state = False

    result = chat_history_collection.delete_many({"user_id": user_id})

    if result.deleted_count > 0:
        state = True
    
    return state

def delete_chat_history_by_workoutplan(workout_plan_id: int):
       
    state = False

    result = chat_history_collection.delete_one({"workout_plan_id": workout_plan_id})

    if result.deleted_count > 0:
        state = True
    
    return state

