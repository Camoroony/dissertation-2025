from sqlmodel import Session, select
from models.db_models import Rating
from models.input_models import RatingInput

def create_rating_db(user_id: int, rating_input: RatingInput, workout_plan_id: int, db: Session):

    rating = Rating(workoutplan_id=workout_plan_id, user_id=user_id, rating=rating_input.rating, comment=rating_input.comment)

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating


def get_rating_db(rating_id: int, db: Session):

    statement = (
        select(Rating)
        .where(Rating.id == rating_id)
    )

    rating = db.exec(statement).first()

    if rating is None:
        raise ValueError(f"Rating entry with ID {rating_id} could not be found.")

    return rating


def get_ratings_by_workout_db(workout_plan_id: int, db: Session):

    statement = (
        select(Rating)
        .where(Rating.workoutplan_id == workout_plan_id)
        .order_by(Rating.id)
    )

    ratings = db.exec(statement).all()

    if not ratings:
        raise ValueError(f"Ratings for the workout with ID {workout_plan_id} could not be found.")

    return ratings




def delete_rating_db(rating_id: int, db: Session):

    statement = (
        select(Rating)
        .where(Rating.id == rating_id)
    )

    rating = db.exec(statement).first()

    if rating is None:
        raise ValueError(f"Rating entry with ID {rating_id} could not be found.")
    else: 
       db.delete(rating)
       db.commit()

    return rating