from typing import Any

from arq.connections import RedisSettings
from pydantic import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str | None

    # Redis backend
    REDIS_HOST: str
    REDIS_PORT: str

    # ARQ Config
    ARQ_REDIS_SETTINGS: RedisSettings | None = None
    ARQ_MAX_JOBS: int = 5
    ARQ_JOB_TIMEOUT: int = 9 * 60 * 60  # 9hrs in seconds
    ARQ_KEEP_RESULT: int = 9 * 60 * 60  # 9hrs in seconds
    ARQ_MAX_TRIES: int = 1
    ARQ_HEALTH_CHECK_INTERVAL: int = 5 * 60  # 5 minutes in seconds
    ARQ_RETRY_JOBS: bool = False
    ARQ_ALLOW_ABORT_JOBS: bool = True

    @validator("ARQ_REDIS_SETTINGS")
    @classmethod
    def assemble_arq_redis_settings(
        cls, value: RedisSettings | None, values: dict[str, Any]
    ) -> RedisSettings:
        if isinstance(value, RedisSettings):
            return value
        settings = RedisSettings(
            host=values["REDIS_HOST"],
            port=values["REDIS_PORT"],
            database=1,
        )
        return settings

    class Config(BaseSettings.Config):
        case_sensitive: bool = True
        env_file: str = ".env"


def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
