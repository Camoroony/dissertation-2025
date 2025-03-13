import json
from models.db_models import WorkoutPlan, WorkoutSession, Exercise
from sqlmodel import Session

def add_workout_plan(workoutplan_data: str, user_id: int, db: Session):

    data = json.loads(workoutplan_data)

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

        for exercise in data["exercises"]:
            exercise_obj = Exercise(
                workoutsession_id = workout_plan_obj.id,
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