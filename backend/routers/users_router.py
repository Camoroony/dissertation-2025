from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session, select
from backend.models.user_model import UserInput, UserSQL, UserBase
from backend.database.database import get_db
from backend.security.hashing import hash_password

router = APIRouter(
    prefix="/users"
)

@router.get("")
def index() :
    return Response ("Hello from the users router!")

@router.get("create-user")
def create_user(user_data: UserInput, db: Session = Depends(get_db)) :
    existing_user = db.exec(select(UserSQL).where(UserInput.username == user_data.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = UserSQL(username=user_data.username, hashed_password=hash_password(user_data.plain_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("get-user")
def index() :
    return Response ("Getting user")

@router.get("update-user")
def index() :
    return Response ("Updating user")

@router.get("delete-user")
def index() :
    return Response ("Deleting user")

