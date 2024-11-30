import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME:str = 'aboba'
    PROJECT_VERSION:str = '1.0.0'

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = (f"postgresql://{POSTGRES_USER}:"
                    f"{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:"
                    f"{POSTGRES_PORT}/{POSTGRES_DB}")

settings = Settings()
