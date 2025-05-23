from pydantic import BaseModel, Field

# Workout plan AI output schema

WORKOUT_PLAN_FUNCTION_SCHEMA = {
    "name": "generate_workout_plan",
    "description": "Generate a structured workout plan following a strict format.",
    "parameters": {
        "type": "object",
        "properties": {
            "plan_name": {
                "type": "string",
                "description": "The name of the overall workout plan."
            },
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
             "experience_level": {
                "type": "string",
                "description": "Experience level required from the individual for the plan."
            },
            "additional_info": {
                "type": "string",
                "description": "Any additional information provided by the user that was considered when making the plan."
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

# Workout plan split schema

WORKOUT_SPLIT_SCHEMA = {
    "name": "define_workout_split",
    "description": "Define a workout split type along with session count and reasoning.",
    "parameters": {
        "type": "object",
        "properties": {
            "split_name": {
                "type": "string",
                "description": "The name of the workout split (e.g., 'Push/Pull/Legs', 'Upper/Lower', 'Full Body')."
            },
            "no_of_sessions": {
                "type": "integer",
                "description": "Total number of sessions per week for this split."
            },
            "split_structure": {
                "type": "array",
                "description": "The structure of the split by day/session, describing what muscle groups or goals are covered.",
                "items": {
                    "type": "object",
                    "properties": {
                        "day": {"type": "string"},
                        "focus": {"type": "string"},
                        "reasoning": {
                            "type": "string",
                            "description": "Why this focus is used on this day and how it complements the overall split."
                        }
                    },
                    "required": ["day", "focus", "reasoning"]
                }
            },
            "split_rationale": {
                "type": "string",
                "description": "Explanation of why this split is chosen, who it's ideal for, and its training advantages."
            }
        },
        "required": ["split_name", "no_of_sessions", "split_structure", "split_rationale"]
    }
}

# Exercise recommendation schema

EXERCISE_RECOMMENDATION_SCHEMA = {
    "name": "structured_muscle_exercises",
    "description": "Provide a structured list of exercises per muscle group including name, equipment, and a brief rationale.",
    "parameters": {
        "type": "object",
        "properties": {
            "muscle_groups": {
                "type": "array",
                "description": "List of muscle groups with corresponding recommended exercises.",
                "items": {
                    "type": "object",
                    "properties": {
                        "muscle": {
                            "type": "string",
                            "description": "Targeted muscle group (e.g., 'Chest', 'Back', etc.)."
                        },
                        "exercises": {
                            "type": "array",
                            "description": "Recommended exercises for the muscle group.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "exercise_name": {
                                        "type": "string",
                                        "description": "Name of the exercise (e.g., 'Bench Press', 'Pull-Up')."
                                    },
                                    "equipment_required": {
                                        "type": "string",
                                        "description": "Type of equipment required (e.g., 'Barbell', 'Resistance Band', 'Bodyweight')."
                                    },
                                    "rationale": {
                                        "type": "string",
                                        "description": "Short reason for recommending the exercise."
                                    }
                                },
                                "required": ["exercise_name", "equipment_required", "rationale"]
                            }
                        }
                    },
                    "required": ["muscle", "exercises"]
                }
            }
        },
        "required": ["muscle_groups"]
    }
}


# Exercise overview AI output schema

class ExerciseOverviewResponse(BaseModel):
    text_tutorial: str = Field(..., description="A written explanation or step-by-step guide")
    video_link: str = Field(..., description="A relevant video tutorial link")

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