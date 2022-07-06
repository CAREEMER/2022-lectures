from pydantic import BaseSettings


class Config(BaseSettings):
    ENVIRONMENT: str = "local"

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5450
    DATABASE_USER: str = "fastapi_db"
    DATABASE_PASSWORD: str = "fastapi_db"
    DATABASE_NAME: str = "fastapi_db"

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )


app_config = Config()
