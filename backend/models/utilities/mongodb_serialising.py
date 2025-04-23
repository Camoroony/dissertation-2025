def serialise_chatId(chat):
    chat["_id"] = str(chat["_id"])
    return chat