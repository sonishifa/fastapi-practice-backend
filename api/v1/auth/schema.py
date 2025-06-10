from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: EmailStr  # Validates email format
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    