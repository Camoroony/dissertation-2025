
# Workout plan AI prompt schema

WORKOUT_PLAN_SCHEMA = """{
  "no_of_sessions": int,  # Total number of workout sessions MUST BE AN INTEGER
  "average_session_length": int,  # Average session length in minutes MUST BE AN INTEGER
  "equipment_requirements": str,  # Equipment required for the plan MUST BE AN STRING
  "workout_sessions": [
    {
      "session_name": str,  # Name of the workout session MUST BE AN STRING
      "length_of_session": int,  # Session duration in minutes MUST BE AN INTEGER
      "day_of_week": str,  # Day the session occurs MUST BE AN STRING
      "equipment_requirements": str,  # Equipment needed MUST BE AN STRING
      "exercises": [
        {
          "exercise_name": str,  # Name of the exercise MUST BE AN STRING
          "sets": int,  # Number of sets MUST BE AN INTEGER
          "reps": int,  # Number of reps per set MUST BE AN INTEGER
          "reps_in_reserve": int  # Reps in reserve MUST BE AN INTEGER
        }
      ]
    }
  ]
}"""