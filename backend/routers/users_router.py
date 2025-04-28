from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session, select
from models.db_models import UserSQL
from models.input_models import UserInput, UserUpdateInput
from models.security_models import Token
from database.sql.init_sql_db import get_db_session
from database.sql.user_sql import update_user_db
from database.mongodb.chat_history_db import create_chat_history, delete_chat_history_by_user
from security.hashing import hash_password, verify_password
from security.jwt_token import verify_token, create_access_token

router = APIRouter(
    prefix="/users"
)

@router.get("/verify-token", response_model=UserSQL)
def verify_token_endpoint(user: UserSQL = Depends(verify_token)):
    return user


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

    create_chat_history(new_user.id, chat_type="General")
    create_chat_history(new_user.id, chat_type="Community")

    return new_user


@router.post("/login-user", response_model=Token, status_code=200)
def login_user(user_data: UserInput, db: Session = Depends(get_db_session)) :
     existing_user = db.exec(select(UserSQL).where(UserSQL.username == user_data.username)).first()
     if not existing_user:
         raise HTTPException(status_code=400, detail="Username does not exist.")
    
     isMatch = verify_password(user_data.plain_password, existing_user.hashed_password)

     if not isMatch:
         raise HTTPException(status_code=400, detail="Incorrect password.")
    
     access_token = create_access_token(
         data={"sub": existing_user.id}
     )
     return {"access_token": access_token, "token_type": "bearer"}


@router.get("/get-user", response_model=UserSQL)
def get_user(user_id: int, db: Session = Depends(get_db_session)) :
    user = db.get(UserSQL, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with id {user_id} exists")
    
    return user


@router.put("/update-user", response_model=UserSQL, status_code=200)
def update_user(updated_user: UserUpdateInput, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    try:
     update_result = update_user_db(updated_user, user.id, db)
    
    except ValueError as e:
      raise HTTPException(status_code=400, detail=str(e))

    return update_result


@router.delete("/delete-user", response_model= str)
def delete_user(user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :
    user = db.get(UserSQL, user.id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with specified token exists")
    
    db.delete(user)
    db.commit()

    delete_chat_history_by_user(user.id)

    return f"Deleted user Id: {user.id}, Username: {user.username}"

