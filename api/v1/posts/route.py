from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.deps import get_db
from api.v1.posts.model import Post
from api.v1.posts.schema import PostCreate, PostOut

router = APIRouter(prefix="/api/v1/posts", tags=["Posts"])

@router.post("/", response_model=PostOut)
def create_post(post_in: PostCreate, db: Session = Depends(get_db)):
    post = Post(title=post_in.title, content=post_in.content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
