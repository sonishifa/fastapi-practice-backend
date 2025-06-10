from fastapi import FastAPI
from db.database import engine
from db.base import Base
from api.v1.users import model as user_model
from api.v1.posts import model as post_model
from api.v1.auth.route import router as auth_router
from api.v1.users.route import router as users_router
from api.v1.posts.route import router as posts_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API", "status": "running"}