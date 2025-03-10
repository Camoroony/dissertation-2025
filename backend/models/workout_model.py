from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import ForeignKey
from typing import List, Optional
from backend.models.user_model import UserSQL

class WorkoutPlan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", sa_column=ForeignKey("user.id", ondelete="CASCADE"))
    no_of_sessions: int
    average_session_length: float
    equipment_requirements: str

    user: UserSQL = Relationship(back_populates="workout_plans")
    workout_sessions = List["WorkoutSession"] = Relationship(back_populates="workout_plan", cascade="all, delete")

class WorkoutSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    workout_id: int = Field(foreign_key="workout.id", sa_column=ForeignKey("workout.id", ondelete="CASCADE"))
    session_name: str
    length_of_session: float
    day_of_week: str
    equipment_requirements: str

    workout_plan: WorkoutPlan = Relationship(back_populates="workout_sessions")
    exercises: List["Exercise"] = Relationship(back_populates="workout_session", cascade="all, delete")

class Exercise(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="workoutsession.id", sa_column=ForeignKey("workoutsession.id", ondelete="CASCADE"))
    exercise_name: str
    sets: int
    reps: int
    reps_in_reserve: Optional[int] = Field(default=0)

    workout_session: WorkoutSession = Relationship(back_populates="exercises")

