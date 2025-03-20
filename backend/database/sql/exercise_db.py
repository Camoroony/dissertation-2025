import json
from models.db_models import WorkoutPlan, WorkoutSession, Exercise
from sqlmodel import Session, select

def get_exercise(exercise_id: int, db: Session):

    exercise = db.exec(select(Exercise).where(Exercise.id == exercise_id)).first() 

    return exercise