from bson import ObjectId
from database.mongodb.init_mongodb_db import get_mongodb_client
from models.ai_models import get_generic_chatbot_sysmessage, get_workoutplan_chatbot_sysmessage
import datetime


db = get_mongodb_client()

chat_history_collection = db['chat_histories']


def create_chat_history(user_id: int, workout_plan_id=None, workout_plan=None):

    chat_history_document = {
        "user_id": user_id,
        "chat_start_time": datetime.datetime.now(datetime.UTC),
        "chats": []
    }

    if workout_plan_id is not None:
        chat_history_document['workout_plan_id'] = workout_plan_id

    result = chat_history_collection.insert_one(chat_history_document)

    new_chat_history = chat_history_collection.find_one({"_id": result.inserted_id})

    return new_chat_history


def add_chat_history(chat_history_id: str, user_message: str, ai_message: str):
    if chat_history_id is None:
      raise ValueError("chat_history_id is null. Must be provided.")
    
    chat_message = {
        "chat_message_id": str(ObjectId()),
        "user_message": user_message,
        "ai_message": ai_message,
        "timestamp": datetime.datetime.now(datetime.UTC)
    }

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
        return {"error": "Chat history not found"}

    return chat_history


def get_chat_histories_by_userid(user_id: int):

    chat_histories = chat_history_collection.find({"user_id": user_id})

    generic_chats = []
    workout_chats = []

    for chat_history in chat_histories:
     if "workout_plan_id" in chat_history:
        workout_chats.append(chat_history)
     else:
        generic_chats.append(chat_history) 

    chats = {
        "generic_chats": generic_chats,
        "workout_chats": workout_chats
    }

    return chats

def delete_chat_history(chat_history_id: int):

    state = False

    result = chat_history_collection.delete_one({"_id": ObjectId(chat_history_id)})

    if result.deleted_count > 0:
        state = True
    
    return state
