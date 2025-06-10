from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core.deps import get_db
from api.v1.auth.domain import AuthenticationDomain
from api.v1.auth.schema import UserRegister
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

auth_domain = AuthenticationDomain()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    return auth_domain.register(user_in, db)


@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Log in a user and return an access token.
    """
    return auth_domain.login(user_credentials, db)
