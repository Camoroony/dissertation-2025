from fastapi import APIRouter, Depends, Response, HTTPException
from sqlmodel import Session
from models.db_models import Rating, UserSQL
from models.input_models import RatingInput
from models.utilities.sql_serialising import serialise_rating
from security.jwt_token import verify_token
from database.sql.init_sql_db import get_db_session
from database.sql.rating_db import create_rating_db, delete_rating_db, get_rating_db, get_ratings_by_workout_db

router = APIRouter(
    prefix="/ratings"
)

@router.get("")
def index() :
    return Response("Hello from the ratings router!")

@router.post("/create-rating", status_code=201)
def create_rating(rating_input: RatingInput, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :
    try:
     rating = create_rating_db(user.id, rating_input, db)
     serialised_rating = serialise_rating(rating)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return serialised_rating

@router.get("/get-rating", response_model=Rating)
def get_rating(rating_id: int, db: Session = Depends(get_db_session)) :
    try:
        rating = get_rating_db(rating_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return rating

@router.get("/get-ratings", response_model=list[Rating])
def get_ratings_by_workout_id(workout_plan_id: int, db: Session = Depends(get_db_session)) :
    try:
        rating = get_ratings_by_workout_db(workout_plan_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return rating

@router.delete("/delete-rating", response_model=Rating)
def delete_rating(rating_id: int, db: Session = Depends(get_db_session)) :
    try:
        rating = delete_rating_db(rating_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return rating