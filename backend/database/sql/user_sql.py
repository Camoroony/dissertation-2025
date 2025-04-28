from models.db_models import UserSQL
from models.input_models import UserUpdateInput
from security.hashing import verify_password, hash_password
from sqlmodel import Session, select


def update_user_db(user_input: UserUpdateInput, user_id: int, db: Session):

    user = db.get(UserSQL, user_id)
    if not user:
        raise ValueError(f"No user with id {user_id} exists")

    isMatch = verify_password(user_input.current_password, user.hashed_password)
    if not isMatch:
        raise ValueError("Incorrect current password.")

    if user_input.new_username:
        if not user_input.confirm_username:
            raise ValueError("Confirmation username is required.")
        if user_input.new_username != user_input.confirm_username:
            raise ValueError("New username and confirmation username do not match.")
        
        existing_user = db.exec(
            select(UserSQL).where(UserSQL.username == user_input.new_username)
        ).first()
        
        if existing_user and existing_user.id != user_id:
            raise ValueError("Username already taken. Please choose another one.")
    
    if user_input.new_password:
        if not user_input.confirm_password:
            raise ValueError("Confirmation password is required.")
        if user_input.new_password != user_input.confirm_password:
            raise ValueError("New password and confirmation password do not match.")

    if user_input.new_username:
        user.username = user_input.new_username

    if user_input.new_password:
        user.hashed_password = hash_password(user_input.new_password)

    db.commit()
    db.refresh(user)

    return user