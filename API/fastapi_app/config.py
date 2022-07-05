from pydantic import BaseSettings


class Config(BaseSettings):
    ENVIRONMENT: str = "local"
    APP_PORT: int = 8000


app_config = Config()
