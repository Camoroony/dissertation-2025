from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator

# User Input Models

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserInput(UserBase):
    plain_password: str


class TrainingExperience(str):
    ALLOWED_LEVELS = {"Beginner (0 - 2 years of experience)", "Intermediate (2 - 5 years of experience)", "Advanced (5+ years of exeprience)"}

    @classmethod
    def validate(cls, value: str):
        if value not in cls.ALLOWED_LEVELS:
            raise ValueError(f"Invalid experience level: {value}. Choose from {cls.ALLOWED_LEVELS}")
        return value 

class WorkoutGenInput(BaseModel):
    experience: TrainingExperience 


    @field_validator("experience", pre=True, always=True)
    def validate_experience(cls, value):
        return TrainingExperience.validate(value)
        

