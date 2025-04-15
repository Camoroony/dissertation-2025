import jwt 
from typing import Optional
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, Request
from sqlmodel import Session
from models.db_models import UserSQL
from database.sql.init_sql_db import get_db_session

JWT_KEY = "secret_key" 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=180)
    to_encode.update({"exp": expire})

    if "sub" in to_encode:
     to_encode["sub"] = str(to_encode["sub"])

    encoded_jwt = jwt.encode(to_encode, JWT_KEY, algorithm="HS256")
    return encoded_jwt

def verify_token(request: Request, db: Session = Depends(get_db_session)) -> UserSQL:
    authorization: Optional[str] = request.headers.get("Authorization")
    
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing.")
    
    parts = authorization.split()

    print(parts[0].lower())
    print(len(parts))
    
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        raise HTTPException(status_code=401, detail="Invalid token format.") # WTF !!!!!!!!!!!
    
    token = parts[1]
    
    try:
        payload = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token.")

    user = db.get(UserSQL, int(user_id))
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    return user  