from sqlalchemy.orm import Session
from api.v1.users.model import User
from api.v1.users.schema import UserCreate
from core.security import get_password_hash


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(
        (User.username == username)
    ).first()
