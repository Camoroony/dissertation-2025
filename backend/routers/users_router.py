import jwt
from typing import Optional
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session, select
from models.db_models import UserSQL
from models.input_models import UserInput
from models.security_models import Token
from database.sql.init_sql_db import get_db_session
from security.hashing import hash_password, verify_password

router = APIRouter(
    prefix="/users"
)


SECRET_KEY = "secret_key" 

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=180)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

@router.get("")
def index() :
    return Response ("Hello from the users router!")

@router.post("/create-user", response_model=UserSQL, status_code=201)
def create_user(user_data: UserInput, db: Session = Depends(get_db_session)) :
    existing_user = db.exec(select(UserSQL).where(UserSQL.username == user_data.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = UserSQL(username=user_data.username, hashed_password=hash_password(user_data.plain_password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login-user", response_model=Token, status_code=201)
def create_user(user_data: UserInput, db: Session = Depends(get_db_session)) :
    # try:
     existing_user = db.exec(select(UserSQL).where(UserSQL.username == user_data.username)).first()
     if not existing_user:
         raise HTTPException(status_code=400, detail="Username does not exist.")
    
     isMatch = verify_password(user_data.plain_password, existing_user.hashed_password)

     if not isMatch:
         raise HTTPException(status_code=400, detail="Incorrect password.")
    
     access_token_expires = timedelta(minutes=180)
     access_token = create_access_token(
         data={"sub": existing_user.id},
         expires_delta=access_token_expires
     )
     return {"access_token": access_token, "token_type": "bearer"}
    
    # except Exception as e:
    #   raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/get-user", response_model=UserSQL)
def get_user(user_id: int, db: Session = Depends(get_db_session)) :
    user = db.get(UserSQL, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with id {user_id} exists")
    
    return user

@router.put("/update-user", response_model=UserSQL)
def update_user(user_id: int, updated_user: UserInput, db: Session = Depends(get_db_session)) :
    user = db.get(UserSQL, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with id {user_id} exists")
    
    for attr, value in updated_user.model_dump().items():
        if attr == "plain_password":
           value = hash_password(value)
           attr = "hashed_password"

        setattr(user, attr, value)

    db.commit()
    db.refresh(user)

    return user

@router.delete("/delete-user", response_model= str)
def delete_user(user_id: int, db: Session = Depends(get_db_session)) :
    user = db.get(UserSQL, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with id {user_id} exists")
    
    db.delete(user)
    db.commit()

    return f"Deleted user Id: {user.id}, Username: {user.username}"

