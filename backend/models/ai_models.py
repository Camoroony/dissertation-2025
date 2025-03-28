from pydantic import BaseModel
from typing import List, Optional


# Workout plan AI prompt schema

WORKOUT_PLAN_FUNCTION_SCHEMA = {
    "name": "generate_workout_plan",
    "description": "Generate a structured workout plan following a strict format.",
    "parameters": {
        "type": "object",
        "properties": {
            "no_of_sessions": {
                "type": "integer",
                "description": "Total number of workout sessions."
            },
            "average_session_length": {
                "type": "integer",
                "description": "Average session length in minutes."
            },
            "equipment_requirements": {
                "type": "string",
                "description": "Equipment required for the plan."
            },
            "workout_sessions": {
                "type": "array",
                "description": "A list of workout sessions included in the plan.",
                "items": {
                    "type": "object",
                    "properties": {
                        "session_name": {"type": "string"},
                        "length_of_session": {"type": "integer"},
                        "day_of_week": {"type": "string"},
                        "equipment_requirements": {"type": "string"},
                        "exercises": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "exercise_name": {"type": "string"},
                                    "sets": {"type": "integer"},
                                    "reps": {"type": "integer"},
                                    "reps_in_reserve": {"type": "integer"}
                                },
                                "required": ["exercise_name", "sets", "reps", "reps_in_reserve"]
                            }
                        }
                    },
                    "required": ["session_name", "length_of_session", "day_of_week", "equipment_requirements", "exercises"]
                }
            }
        },
        "required": ["no_of_sessions", "average_session_length", "equipment_requirements", "workout_sessions"]
    }
}

# AI prompt defintions

MUSCLE_GROUPS = ["Chest", "Shoulders", "Back", "Biceps", "Triceps", "Core\\Abs", "Leg (Quads/Hamstrings/Calfs)"]