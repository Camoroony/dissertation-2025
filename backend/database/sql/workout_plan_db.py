import json
from typing import Dict, Any
from models.db_models import WorkoutPlan, WorkoutSession, Exercise
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

def add_workout_plan(data: Dict[str, Any], user_id: int, db: Session):

    workout_plan_obj = WorkoutPlan(
        user_id = user_id,
        no_of_sessions = data["no_of_sessions"],
        average_session_length = data["average_session_length"],
        equipment_requirements = data["equipment_requirements"]

    )

    db.add(workout_plan_obj)
    db.flush()

    workout_sessions = []

    for workoutsession in data["workout_sessions"]:
        workout_session_obj = WorkoutSession(
            workoutplan_id = workout_plan_obj.id,
            session_name = workoutsession["session_name"],
            length_of_session = workoutsession["length_of_session"],
            day_of_week = workoutsession["day_of_week"],
            equipment_requirements = workoutsession["equipment_requirements"]
        )

        db.add(workout_session_obj)
        db.flush()

        exercises = []

        for exercise in workoutsession["exercises"]:
            exercise_obj = Exercise(
                workoutsession_id = workout_session_obj.id,
                exercise_name = exercise["exercise_name"],
                sets = exercise["sets"],
                reps = exercise["reps"],
                reps_in_reserve = exercise["reps_in_reserve"]
            )

            exercises.append(exercise_obj)
            db.add(exercise_obj)
        
        workout_sessions.append(workout_session_obj)

    db.commit()

    return workout_plan_obj

def get_workout_plan(workout_plan_id: int, db: Session):

    statement = (
        select(WorkoutPlan)
        .where(WorkoutPlan.id == workout_plan_id)
        .options(
            selectinload(WorkoutPlan.workout_sessions).selectinload(WorkoutSession.exercises)
        )
    )

    workout_plan = db.exec(statement).first()

    return workout_plan

def delete_workout_plan(workout_plan_id: int, db: Session):

    state = False

    workout_plan = db.exec(select(WorkoutPlan).where(WorkoutPlan.id == workout_plan_id)).first()

    if workout_plan:
        db.delete(workout_plan)
        db.commit()
        state = True

    return state
