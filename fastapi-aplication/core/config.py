from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings  , SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatebaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False, # Нижний регистер
        env_nested_delimiter="__", # разделитель
        env_prefix="APP_CONFIG__", # начало переменной окружения
        env_file=".env" # файл переменных
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatebaseConfig

settings = Settings()