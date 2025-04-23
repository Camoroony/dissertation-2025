from fastapi import APIRouter, Depends, Response, HTTPException
from sqlmodel import Session
from database.sql.init_sql_db import get_db_session
from database.mongodb.chat_history_db import create_chat_history, get_chat_history, add_chat_history, delete_chat_history, get_chat_histories_by_userid
from database.sql.workout_plan_db import get_workout_plan, get_workout_plans
from models.utilities.sql_serialising import serialise_workout_plan
from models.utilities.mongodb_serialising import serialise_chatId
from models.db_models import UserSQL
from models.input_models import UserChatInput
from security.jwt_token import verify_token
from ai_services.gen_chat import generate_chat, generate_community_chat

router = APIRouter(
    prefix="/chatbot"
)

@router.get("")
def index() :
    return Response("Hello from the chatbot router!")


@router.post("/chat")
def chat(userInput: UserChatInput, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
      raise HTTPException(f"User Token verification failed")
    
    try: 

     chat_history = get_chat_history(userInput.chat_history_id)

     workout_plans_dict = []

     if chat_history['chat_type'] == "Community":

      workout_plans = get_workout_plans(db)
 
      for workout_plan in workout_plans:
           serialised_workout_plan = serialise_workout_plan(workout_plan)
           workout_plans_dict.append(serialised_workout_plan)

     workout_plan_id = chat_history.get("workout_plan_id", None)

     workout_plan = get_workout_plan(workout_plan_id, user.id, db) if workout_plan_id is not None else None
     workout_plan_dict = serialise_workout_plan(workout_plan) if workout_plan else None

     ai_response_data = generate_chat(userInput.user_prompt, chat_history, workout_plans_dict, workout_plan_dict)
    
     add_chat_history(chat_history["_id"], userInput.user_prompt, ai_response_data["ai_response"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
    return ai_response_data


@router.post("/community-chat")
def community_chat(user_id: int, user_prompt: str, chat_history_id=None, db: Session = Depends(get_db_session)) :

    try: 
     workout_plans = get_workout_plans(db)

     workout_plans_dict = []
 
     for workout_plan in workout_plans:
         serialised_workout_plan = serialise_workout_plan(workout_plan)
         workout_plans_dict.append(serialised_workout_plan)

     chat_history = create_chat_history(user_id, chat_type="community") if chat_history_id is None else get_chat_history(chat_history_id)

     ai_response_data = generate_community_chat(user_prompt, chat_history, workout_plans_dict)

     add_chat_history(chat_history["_id"], user_prompt, ai_response_data["ai_response"])

     return ai_response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@router.get("/get-chat-history", status_code=200)
def get_chat_history_by_user(user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
      raise HTTPException(f"User Token verification failed")
    
    try: 
     chat_histories = get_chat_histories_by_userid(user.id)

     serialised_chat_histories = [serialise_chatId(chat_history) for chat_history in chat_histories]

    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Error when retrieving chat history: {str(e)}")
    
    return serialised_chat_histories 


@router.delete("/delete-chat")
def delete_chat(chat_history_id: str):
    
    response = delete_chat_history(chat_history_id)

    if response is False:
        raise HTTPException(f"Error occured when deleting chat history ID: {chat_history_id}")
    
    return Response(f"Chat history Id: ({chat_history_id}) deleted")