from sqlalchemy.orm import Session
from api.v1.posts.model import Post
from api.v1.posts.schema import PostCreate

class PostRepository:
    def create_post(self, post_in: PostCreate, db: Session):
        post = Post(title=post_in.title, content=post_in.content)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    def get_post_by_id(self, post_id: int, db: Session):
        return db.query(Post).filter(Post.id == post_id).first()

    def get_all_posts(self, db: Session):
        return db.query(Post).all()
