from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'
    DATABASE_URL: str = "mysql+aiomysql://root:Dev2020@@127.0.0.1/library"
    DATABASE_BaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()
