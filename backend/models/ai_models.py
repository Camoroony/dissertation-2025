from pydantic import BaseModel, Field

# Workout plan AI output schema

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

# Exercise overview AI output schema

class ExerciseOverviewResponse(BaseModel):
    text_tutorial: str = Field(..., description="A written explanation or step-by-step guide")
    video_link: str = Field(..., description="A relevant video tutorial link")

# General chatbot chat history system message 

def get_generic_chatbot_sysmessage():

    message = (
    "You are a chatbot who answers questions regarding muscular hypertrophy and other muscle building question."
    )
    
    return message

# Workout plan chatbot chat history system message 

def get_workoutplan_chatbot_sysmessage(workout_plan):

    message = (
    "You are a chatbot who answers questions regarding a workout plan."
    f"\n This is the workout plan you answer questions about: {workout_plan}"
    )
    
    return message


# Sets per muscle group AI prompt schema

MUSCLE_GROUP_SETS_SCHEMA = {
    "name": "generate_muscle_group_sets",
    "description": "Generate a structured dictionary mapping muscle groups to the number of sets to perform.",
    "parameters": {
        "type": "object",
        "properties": {
            "muscle_groups": {
                "type": "object",
                "description": "A dictionary where keys are muscle group names and values are the number of sets.",
                "additionalProperties": {
                    "type": "integer",
                    "description": "Number of sets for the muscle group."
                }
            }
        },
        "required": ["muscle_groups"]
    }
}

# AI prompt defintions

MUSCLE_GROUPS = ["Chest", "Shoulders", "Back", "Biceps", "Triceps", "Core\\Abs", "Legs (Quads/Hamstrings/Calfs)"]

INDIVIDUAL_MUSCLES = ("Chest", "Shoulders", "Back", "Biceps", "Triceps", "Core\\Abs", "Quads", "Hamstrings", "Glutes", "Calfs")