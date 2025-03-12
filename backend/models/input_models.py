from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator, model_validator
from typing import List

# User Input Models

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserInput(UserBase):
    plain_password: str

# Workout Plan Input Type Validators

EXPERIENCE_LEVELS = {"Beginner (0 - 2 years of experience)", "Intermediate (2 - 5 years of experience)", "Advanced (5+ years of exeprience)"}
AVAILABILITY_DAYS = range(1, 6)
SESSION_LENGTH = range(10, 90)
TRAINING_FOCUS = {"Full-Body", "Upper-Body", "Lower-Body", "Arms", "Shoulders", "Chest", "Back"}
AVAILABLE_EQUIPMENT = {
    "Dumbbells", "Barbell",
    "Squat Rack", "Power Rack", "Smith Machine", "Leg Press Machine", 
    "Cable Machine", "Chest Press Machine", "Lat Pulldown Machine", 
    "Seated Row Machine", "Hack Squat Machine", "Leg Extension Machine", 
    "Leg Curl Machine", "Incline Bench", "Flat Bench", "Decline Bench", 
    "Preacher Curl Bench", "Dip Bar", "Pull-Up Bar", 
    "Smith Machine", "Barbell Plate", "Bicep Curl Machine", 
    "Triceps Pushdown Machine", "Seated Calf Raise Machine", 
    "Lateral Raise Machine", "Glute Bridge Machine", "Abdominal Crunch Machine"
}

# Workout Plan Input Model

class WorkoutGenInput(BaseModel):
    experience_level: str
    training_availability: int
    session_length: int
    training_focus: str 
    available_equipment: List[str]  # List of equipment the user is using
    additional_info : str

    @field_validator("experience_level")
    def validate_experience_level(cls, value):
        if value not in EXPERIENCE_LEVELS:
            raise ValueError(f"Invalid experience level: {value}. Allowed levels are: {', '.join(EXPERIENCE_LEVELS)}")
        return value
    
    @field_validator("training_experience")
    def validate_experience_level(cls, value):
        if value not in AVAILABILITY_DAYS:
            raise ValueError(f"Training availability must be between 1 and 5 days per week. Got {value}.")
        return value
    
    @field_validator("session_length")
    def validate_experience_level(cls, value):
        if value not in SESSION_LENGTH:
            raise ValueError(f"Session length must be between 10 and 90 minutes. Got {value} minutes.")
        return value
    
    @field_validator("training_focus", mode="before")
    def validate_experience_level(cls, value):
        if value not in TRAINING_FOCUS:
            raise ValueError(f"Invalid training focus category: {value}. Allowed categories are: {', '.join(TRAINING_FOCUS)}")
        return value
    
    @model_validator(mode="before")
    def validate_available_equipment(cls, values):
        available_equipment_input = values.get('available_equipment', [])
        
        # Check if all items in the list are valid equipment
        invalid_items = [item for item in available_equipment_input if item not in AVAILABLE_EQUIPMENT]
        
        if invalid_items:
            raise ValueError(f"Invalid equipment type(s): {', '.join(invalid_items)}")
        
        return values




        

