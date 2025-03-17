from fastapi import APIRouter, Depends, Response
from sqlmodel import Session
from database.sql.init_sql_db import get_db_session
from database.mongodb.chat_history_db import get_chat_history, add_chat_history
from database.sql.workout_plan_db import get_workout_plan
from ai.gen_chat import generate_chat

router = APIRouter(
    prefix="/chatbot"
)

@router.get("")
def index() :
    return Response("Hello from the chatbot router!")

@router.post("/chat")
def workout_chat(user_id: int, user_prompt: str, chat_history_id=None, workout_plan_id=None, db: Session = Depends(get_db_session)) :

    chat_history = get_chat_history(chat_history_id) if chat_history_id is not None else None

    workout_plan = get_workout_plan(workout_plan_id, db) if workout_plan_id is not None else None

    ai_response_data = generate_chat(user_prompt, chat_history, workout_plan)

    add_chat_history(user_id, user_prompt, ai_response_data, chat_history_id, workout_plan_id)

    return ai_response_data