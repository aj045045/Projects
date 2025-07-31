from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class EnvSettings(BaseSettings):
    """
    Environment variables configuration.
    Auto-loads from .env file and system environment.
    """

    OLLAMA_MODEL: str = Field(...)
    OLLAMA_EMBEDDING_MODEL: str = Field(...)

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


env_settings = EnvSettings()

__all__ = ["env_settings"]
