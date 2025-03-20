from models.db_models import WorkoutPlan, WorkoutSession, Exercise
from typing import Dict, Any

def serialise_workout_plan(workout_plan: WorkoutPlan) -> Dict[str, Any]:

        if not workout_plan:
            return {"error": "Workout plan not found for serialisation"}

        return {
            "id": workout_plan.id,
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


def serialise_exercise(exercise: Exercise) -> Dict[str, Any]:
      
       if not exercise:
            return {"error": "Exercise not found for serialisation"}
       
       return {
              "id": exercise.id,
              "exercise_name": exercise.exercise_name,
              "sets": exercise.sets,
              "reps": exercise.reps,
              "reps_in_reserve": exercise.reps_in_reserve
       }
      