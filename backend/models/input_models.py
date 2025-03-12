from sqlmodel import SQLModel, Field
from pydantic import BaseModel, model_validator

# User Input Models

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserInput(UserBase):
    plain_password: str

# Workout Plan Input Type Validators

ALLOWED_LEVELS = {"Beginner (0 - 2 years of experience)", "Intermediate (2 - 5 years of experience)", "Advanced (5+ years of exeprience)"}

# Workout Plan Input Model

class WorkoutGenInput(BaseModel):
    experience_level: str
    training_availability: int
    session_length: int
    training_focus: str 
    available_equipment: str 
    additional_info : str



        

