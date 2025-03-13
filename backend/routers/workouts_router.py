from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session
from database.sql.sqldatabase import get_db_session
from database.add_workout_plan import add_workout_plan
from database.workout_contexts import add_workout_context
from models.input_models import WorkoutGenInput
from ai.gen_workout_plan import generate_workout_plan
from ai.gen_workout_info import generate_exercise_overview

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

@router.get("/get-exercise-info")
def get_exercise_info(exercise_id: int, workout_plan_id: int, db: Session = Depends(get_db_session)) :

    # ai_response_data = generate_exercise_overview()

    return Response()