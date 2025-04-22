def serialize_chatId(chat):
    chat["_id"] = str(chat["_id"])  # or whatever field holds ObjectId
    return chat