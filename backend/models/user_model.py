from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)

class UserSQL(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserInput(UserBase):
    plain_password: str
