from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.v1.users.model import User
from core.security import verify_password, get_password_hash
from .oauth2 import create_access_token
from ..users.repository import (
    get_user_by_username
)

class AuthenticationRepository:
    def login(self, user_credentials, db: Session):
        user = get_user_by_username(db, user_credentials.username)
        
        if not user or not verify_password(user_credentials.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid username or password"
            )
        
        token = create_access_token(data={"user_id": user.id})
        return {
            "access_token": token,
            "token_type": "bearer",
            "user_id": user.id
        }

    def register(self, user_in, db: Session):
        existing_user = get_user_by_username(db, user_in.username)
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email already exists"
            )
        
        hashed_pw = get_password_hash(user_in.password)
        new_user = User(
            username=user_in.username,
            email=user_in.email,
            hashed_password=hashed_pw
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
