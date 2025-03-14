from bson import ObjectId
from database.mongodb.init_mongodb_db import get_mongodb_client
import datetime


db = get_mongodb_client()

chat_history_collection = db["chat_histories"]


def create_chat_history(user_id: int):

    chat_history_document = {
        "user_id": user_id,
        "chat_start_time": datetime.datetime.now(datetime.UTC),
        "chats": []
    }

    result = chat_history_collection.insert_one(chat_history_document)

    return result.inserted_id


def add_chat_history(user_id: int, user_message: str, ai_message: str, chat_history_id=None):
    if chat_history_id is None:
        chat_history_id = create_chat_history(user_id)
    
    chat_message = {
        "chat_message_id": str(ObjectId()),
        "user_message": user_message,
        "ai_message": ai_message,
        "timestamp": datetime.datetime.now(datetime.UTC)
    }

    result = chat_history_collection.update_one(
        {"_id": ObjectId(chat_history_id)},
        {"$push": {"chats": chat_message}}
    )
        
    return f"Chat message (Id: {result}) added to chat history (Id: {chat_history_id}) "

def get_chat_history(chat_history_id: int):

    chat_history = chat_history_collection.find_one(
        {"_id": ObjectId(chat_history_id)},
        {"_id": 0, "chats": 1} 
    )

    if not chat_history:
        return {"error": "Chat history not found"}
    
    messages = []

    for chat in chat_history["chats"]:
        messages.append(f"User: {chat["user_message"]}")
        messages.append(f"Response: {chat["ai_message"]}")

    return messages

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
