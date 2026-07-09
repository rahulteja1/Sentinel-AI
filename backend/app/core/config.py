"""
Sentinel AI Configuration

Centralized application configuration.
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "Sentinel AI"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # API
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Database
    DATABASE_URL: str = "sqlite:///./sentinel.db"

    # AI
    LLM_PROVIDER: str = "ollama"
    LLM_MODEL: str = "qwen2.5:7b"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Security
    SECRET_KEY: str = Field(...)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    @property
    def DATA_DIR(self) -> Path:
        return BASE_DIR / "data"

    @property
    def LOG_DIR(self) -> Path:
        return BASE_DIR / "logs"

    @property
    def VECTOR_DIR(self) -> Path:
        return BASE_DIR / "data" / "vector_store"


settings = Settings()