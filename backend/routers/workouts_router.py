from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session, select
from database.database import get_db
from models.input_models import WorkoutGenInput

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")

@router.post("/create-workout-plan")
def create_workout(workout_input: WorkoutGenInput, db: Session = Depends(get_db)) :

    workoutInput = workout_input

    return Response("Creating workout plan!")