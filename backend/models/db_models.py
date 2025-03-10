from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import ForeignKey
from typing import List, Optional

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserInput(UserBase):
    plain_password: str

class UserSQL(UserBase, table=True):

    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

    workout_plans: List["WorkoutPlan"] = Relationship(back_populates="user")

class WorkoutPlan(SQLModel, table=True):

    __tablename__ = "workoutplan"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    no_of_sessions: int
    average_session_length: float
    equipment_requirements: str

    user: UserSQL = Relationship(back_populates="workout_plans")
    workout_sessions: List["WorkoutSession"] = Relationship(back_populates="workout_plan")
    

class WorkoutSession(SQLModel, table=True):

    __tablename__ = "workoutsession"

    id: Optional[int] = Field(default=None, primary_key=True)
    workout_id: int = Field(foreign_key="workoutplan.id")
    session_name: str
    length_of_session: float
    day_of_week: str
    equipment_requirements: str

    workout_plan: WorkoutPlan = Relationship(back_populates="workout_sessions")
    exercises: List["Exercise"] = Relationship(back_populates="workout_session")

class Exercise(SQLModel, table=True):

    __tablename__ = "exercise"

    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="workoutsession.id")
    exercise_name: str
    sets: int
    reps: int
    reps_in_reserve: Optional[int] = Field(default=0)

    workout_session: WorkoutSession = Relationship(back_populates="exercises")

