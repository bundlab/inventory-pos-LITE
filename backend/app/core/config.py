from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Add these fields so Pydantic picks them up from Docker
    DATABASE_URL: str 
    SECRET_KEY: str
    CORS_ORIGINS: List[str] = []

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        return v

    # This tells Pydantic to read from environment variables
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env" 
    )

settings = Settings()