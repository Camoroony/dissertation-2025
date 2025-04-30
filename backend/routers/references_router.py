from fastapi import APIRouter, Depends, Response, HTTPException
from sqlmodel import Session
from database.sql.init_sql_db import get_db_session
from database.mongodb.references_db import get_references
from models.db_models import UserSQL
from security.jwt_token import verify_token


router = APIRouter(
    prefix="/references"
)

@router.get("")
def index() :
    return Response("Hello from the ratings router!")

@router.get("/get-references", status_code=200)
def retrieve_references(user: UserSQL = Depends(verify_token)) :

    if not user: 
        HTTPException("User Token verification failed")

    try:
        references = get_references()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f'{e}')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'An unknown error has occured when fetching references: {e}')

    return references
