from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:shifaap@localhost:5432/fastapi_db"

    class Config:
        env_file = ".env"

settings = Settings()
