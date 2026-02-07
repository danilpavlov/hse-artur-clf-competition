from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydantic import Field


class Settings(BaseSettings):
    
    FEATURES_SAVE_DIR: str = Field('./data/feature', description="Директория куда будут сохранятся фичи")
    
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    
    
    
@lru_cache
def get_config() -> Settings:
    return Settings()