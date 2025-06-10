from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
