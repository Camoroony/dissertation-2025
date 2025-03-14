from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session
from database.sql.init_sql_db import get_db_session
from database.sql.workout_plan_db import add_workout_plan
from pymongo import database
from database.mongodb.workout_context_db import add_workout_context, get_workout_context
from models.input_models import WorkoutGenInput
from ai.gen_workout_plan import generate_workout_plan
from ai.gen_workout_info import generate_exercise_overview, generate_workoutsession_overview

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")

@router.post("/create-workout-plan")
def create_workout(workout_input: WorkoutGenInput, user_id: int, db: Session = Depends(get_db_session)) :

    ai_response_data = generate_workout_plan(workout_input)

    add_result_sql = add_workout_plan(ai_response_data["response"], user_id, db)

    add_result_mongodb = add_workout_context(add_result_sql.id, ai_response_data["context"])

    return Response(
        f"Created workout plan {add_result_sql} for user: {add_result_sql.user_id}\n"
        f"Workout context {add_result_mongodb["status"]}, Id: {add_result_mongodb["inserted_id"]}",
        status_code=200
    )

@router.get("/get-workoutsession-info")
def get_workoutsession_info(workout_plan_id: int , workoutsession_id: int) :

    context = get_workout_context(workout_plan_id)

    ai_response_data = generate_workoutsession_overview(context, workoutsession_id)

    return Response(ai_response_data, status_code=200)

@router.get("/get-exercise-info")
def get_exercise_info(workout_plan_id: int , exercise_id: int) :

    context = get_workout_context(workout_plan_id)

    ai_response_data = generate_exercise_overview(context, exercise_id)

    return Response(ai_response_data, status_code=200)