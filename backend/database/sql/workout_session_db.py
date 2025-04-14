from models.db_models import WorkoutSession
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload


def get_workout_session(workout_session_id: int, db: Session):

    statement = (
        select(WorkoutSession)
        .where(WorkoutSession.id == workout_session_id)
        .options(selectinload(WorkoutSession.exercises))
    )

    workout_session = db.exec(statement).first()

    if workout_session is None:
        raise ValueError(f"Workout session with ID {workout_session_id} not found.")

    return workout_session