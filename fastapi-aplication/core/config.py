from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings  

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatebaseConfig(BaseModel):
    url: PostgresDsn

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatebaseConfig = DatebaseConfig()

settings = Settings()\
