from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SEKRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()