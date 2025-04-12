from fastapi import APIRouter, Depends, Response, HTTPException
from sqlmodel import Session
from database.sql.init_sql_db import get_db_session
from database.mongodb.chat_history_db import create_chat_history, get_chat_history, add_chat_history, delete_chat_history
from database.sql.workout_plan_db import get_workout_plan
from models.utilities.sql_seralising import serialise_workout_plan
from ai_services.gen_chat import generate_chat

router = APIRouter(
    prefix="/ratings"
)

@router.get("")
def index() :
    return Response("Hello from the ratings router!")