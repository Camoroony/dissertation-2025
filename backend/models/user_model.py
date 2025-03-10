from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from backend.models.workout_model import WorkoutPlan

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserSQL(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

    workout_plans: List["WorkoutPlan"] = Relationship(back_populates="user", cascade="all, delete")

class UserInput(UserBase):
    plain_password: str
