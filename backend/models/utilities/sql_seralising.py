from models.db_models import WorkoutPlan, WorkoutSession, Exercise
from typing import Dict, Any

def serialise_workout_plan(workout_plan: WorkoutPlan) -> Dict[str, Any]:

        if not isinstance(workout_plan, WorkoutPlan):
          raise TypeError("Object must be of type WorkoutPlan to be serialised.")

        return {
            "id": workout_plan.id,
            "plan_name": workout_plan.plan_name,
            "user_id": workout_plan.user_id,
            "no_of_sessions": workout_plan.no_of_sessions,
            "average_session_length": workout_plan.average_session_length,
            "equipment_requirements": workout_plan.equipment_requirements,
            "workout_sessions": [
                {
                    "id": session.id,
                    "session_name": session.session_name,
                    "length_of_session": session.length_of_session,
                    "day_of_week": session.day_of_week,
                    "equipment_requirements": session.equipment_requirements,
                    "exercises": [
                        {
                            "id": exercise.id,
                            "exercise_name": exercise.exercise_name,
                            "sets": exercise.sets,
                            "reps": exercise.reps,
                            "reps_in_reserve": exercise.reps_in_reserve
                        }
                        for exercise in session.exercises
                    ]
                }
                for session in workout_plan.workout_sessions
            ]
        }

def serialise_workout_session(workout_session: WorkoutSession):

    if not isinstance(workout_session, WorkoutSession):
      raise TypeError("Object must be of type WorkoutSession to be serialised.")

    return {
        "id": workout_session.id,
        "session_name": workout_session.session_name,
        "length_of_session": workout_session.length_of_session,
        "day_of_week": workout_session.day_of_week,
        "equipment_requirements": workout_session.equipment_requirements,
        "exercises": [
            {
                "exercise_name": exercise.exercise_name,
                "sets": exercise.sets,
                "reps": exercise.reps,
                "reps_in_reserve": exercise.reps_in_reserve
            }
            for exercise in workout_session.exercises
        ]
    }



def serialise_exercise(exercise: Exercise) -> Dict[str, Any]:
      
    if not isinstance(exercise, Exercise):
      raise TypeError("Object must be of type Exercise to be serialised.")
       
    return {
        "id": exercise.id,
        "exercise_name": exercise.exercise_name,
        "sets": exercise.sets,
        "reps": exercise.reps,
        "reps_in_reserve": exercise.reps_in_reserve
       }
      