
# Workout plan AI prompt schema

WORKOUT_PLAN_SCHEMA = """{{
  "no_of_sessions": int,  # Total number of workout sessions
  "average_session_length": int,  # Average session length in minutes
  "equipment_requirements": str,  # Equipment required for the plan
  "workout_sessions": [
    {{
      "session_name": str,  # Name of the workout session
      "length_of_session": int,  # Session duration in minutes
      "day_of_week": str,  # Day the session occurs
      "equipment_requirements": str,  # Equipment needed
      "exercises": [
        {{
          "exercise_name": str,  # Name of the exercise
          "sets": int,  # Number of sets
          "reps": int,  # Number of reps per set
          "reps_in_reserve": int  # Reps in reserve
        }}
      ]
    }}
  ]
}}"""