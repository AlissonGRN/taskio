from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    SECRET_KEY: str = "ASUH86152jashd!@#asdhASDhasd"  # Default para dev, mude em produção
    DATABASE_URL: str = "sqlite+aiosqlite:///./tasks.db"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
