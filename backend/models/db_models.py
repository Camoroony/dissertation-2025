from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import ForeignKey
from typing import List, Optional
from pydantic import BaseModel, field_validator
from models.input_models import UserBase

# User SQL Models 

class UserSQL(UserBase, table=True):

    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

    workout_plans: List["WorkoutPlan"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "delete"})
    ratings: List["Rating"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "delete"})

# Workout SQL Models 

class WorkoutPlan(SQLModel, table=True):

    __tablename__ = "workoutplan"

    id: Optional[int] = Field(default=None, primary_key=True)
    plan_name: str 
    user_id: int = Field(foreign_key="user.id")
    no_of_sessions: int
    average_session_length: int
    equipment_requirements: str

    user: UserSQL = Relationship(back_populates="workout_plans")
    workout_sessions: List["WorkoutSession"] = Relationship(back_populates="workout_plan", sa_relationship_kwargs={"cascade": "delete"})
    ratings: List["Rating"] = Relationship(back_populates="workout_plan", sa_relationship_kwargs={"cascade": "delete"})
    

class WorkoutSession(SQLModel, table=True):

    __tablename__ = "workoutsession"

    id: Optional[int] = Field(default=None, primary_key=True)
    workoutplan_id: int = Field(foreign_key="workoutplan.id")
    session_name: str
    length_of_session: int
    day_of_week: str
    equipment_requirements: str

    workout_plan: WorkoutPlan = Relationship(back_populates="workout_sessions")
    exercises: List["Exercise"] = Relationship(back_populates="workout_session", sa_relationship_kwargs={"cascade": "delete"})

class Exercise(SQLModel, table=True):

    __tablename__ = "exercise"

    id: Optional[int] = Field(default=None, primary_key=True)
    workoutsession_id: int = Field(foreign_key="workoutsession.id")
    exercise_name: str
    sets: int
    reps: int
    reps_in_reserve: Optional[int] = Field(default=0)

    workout_session: WorkoutSession = Relationship(back_populates="exercises", sa_relationship_kwargs={"cascade": "delete"})

# Workout ratings table

class Rating(SQLModel, table=True):

    __tablename__ = "rating"

    id: Optional[int] = Field(default=None, primary_key=True)
    workoutplan_id: int = Field(foreign_key="workoutplan.id")
    user_id: int = Field(foreign_key="user.id")
    rating: bool
    comment: str

    workout_plan: WorkoutPlan = Relationship(back_populates="ratings", sa_relationship_kwargs={"cascade": "delete"})
    user: UserSQL = Relationship(back_populates="ratings", sa_relationship_kwargs={"cascade": "delete"})