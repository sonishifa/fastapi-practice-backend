from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.deps import get_db
from api.v1.users.model import User
from api.v1.users.schema import UserCreate, UserOut
from passlib.context import CryptContext

router = APIRouter(prefix="/api/v1/users", tags=["Users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=UserOut)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = pwd_context.hash(user_in.password)
    user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
