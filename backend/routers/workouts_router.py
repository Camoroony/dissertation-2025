from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session, select
from database.database import get_db
from models.input_models import WorkoutGenInput
from AI.gen_workout_plan import generate_workout_plan

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")

@router.post("/create-workout-plan")
def create_workout(workout_input: WorkoutGenInput, db: Session = Depends(get_db)) :

    ai_response = generate_workout_plan(workout_input)

    return Response(ai_response)