from backend.database.mongodb.init_mongodb_db import get_mongodb_client

db = get_mongodb_client()

def add_chat_history():

    return "Adding chat history!"


def get_chat_history():

    return "Getting chat history!"