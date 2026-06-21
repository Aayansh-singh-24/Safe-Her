from pydantic_settings import SettingsConfigDict,BaseSettings

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file="app/.env",extra="ignore")
    DATABASE_URL : str


setting = Setting()