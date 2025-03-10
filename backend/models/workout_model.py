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