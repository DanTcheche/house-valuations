import logging
from functools import lru_cache
from typing import Any, List, Union

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=".env", env_file_encoding="utf-8"
    )
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "House Valuations"
    BACKEND_CORS_ORIGINS: Union[str, List[Any]] = []
    REQUESTS_TIMEOUT_SECONDS: int = 10
    PROVIDER_1_API_KEY: str
    PROVIDER_2_API_KEY: str
    PROVIDER_1_ENDPOINT: str
    PROVIDER_2_ENDPOINT: str

    # Logging
    LOG_JSON_FORMAT: bool = False
    LOG_LEVEL: int = logging.INFO

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()


@lru_cache()
def get_settings():
    return settings
