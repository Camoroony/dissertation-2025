from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator, model_validator
from typing import Optional

# User Input Models

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserLoginInput(UserBase):
    plain_password: str

class UserCreateInput(UserLoginInput):
    confirm_password: str

class UserUpdateInput(BaseModel):
    new_username: str
    confirm_username: str
    new_password: str
    confirm_password: str
    current_password: str

# Workout Plan Input Type Validators

EXPERIENCE_LEVELS = {"Beginner (less than 12 months of consistent, proper training experience)",
                      "Intermediate (1 to 4 years of consistent, proper training experience)",
                        "Advanced (more than 4 years of consistent, proper training experience)"}
AVAILABILITY_DAYS = range(1, 6)
SESSION_LENGTH = range(10, 90)
TRAINING_FOCUS = {"Full-Body", "Upper-Body", "Lower-Body", "Arms", "Shoulders", "Chest", "Back"}
AVAILABLE_EQUIPMENT = {
    "Full gym access",
    "Dumbbells", "Bodyweight"
}

# Workout Plan Input Model

class WorkoutGenInput(BaseModel):
    experience_level: str
    training_availability: int
    training_focus: str 
    available_equipment: str 
    additional_info : Optional[str] = None

    @field_validator("experience_level", mode="before")
    def validate_experience_level(cls, value):
        if value is None or value is "":
            raise ValueError("Please provide an experience level")
        if value not in EXPERIENCE_LEVELS:
            raise ValueError(f"Invalid experience level: {value}. Allowed levels are: {', '.join(EXPERIENCE_LEVELS)}")
        return value
    
    @field_validator("training_availability", mode="before")
    def validate_training_experience(cls, value):
        if value is None or value is "":
            raise ValueError("Please provide an availability time")
        if value not in AVAILABILITY_DAYS:
            raise ValueError(f"Training availability must be between 1 and 5 days per week. Got {value}.")
        return value
    
    @field_validator("training_focus", mode="before")
    def validate_training_focus(cls, value):
        if value is None or value is "":
            raise ValueError("Please provide a training focus")
        if value not in TRAINING_FOCUS:
            raise ValueError(f"Invalid training focus category: {value}. Allowed categories are: {', '.join(TRAINING_FOCUS)}")
        return value
    
    @field_validator("available_equipment", mode="before")
    def validate_available_equipment(cls, value):
        if value is None or value is "":
            raise ValueError("Please provide an equipment availability option")
        if value not in AVAILABLE_EQUIPMENT:
            raise ValueError(f"Invalid equipment type: {value}, allowed categories are {', '.join(AVAILABLE_EQUIPMENT)}")
        
        return value


# Rating Input Models

class RatingInput(BaseModel):
    rating: bool
    comment: str
    workout_plan_id: int


# User Chat Input Model

class UserChatInput(BaseModel):
    user_prompt: str
    chat_history_id: str