from pydantic_settings import BaseSettings,SettingsConfigDict
class Setting(BaseSettings):
    llm_api_key:str
    model_config=SettingsConfigDict(
        env_file=".env"
    )
setting=Setting()
