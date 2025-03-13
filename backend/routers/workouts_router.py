from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session
from database.sql.sqldatabase import get_db_session
from database.add_workout_plan import add_workout_plan
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

    add_result = add_workout_plan(ai_response_data, user_id, db)

    return Response(f"Created workout plan {add_result} for user: {add_result.user_id}")


@router.get("/get-exercise-info")
def get_exercise_info(exercise_id: int, workout_plan_id: int, db: Session = Depends(get_db_session)) :

    # ai_response_data = generate_exercise_overview()

    return Response()