import pydantic
import pydantic_settings
from pydantic_settings import BaseSettings 
from pydantic import Field, SecretStr, HttpUrl
from pydantic_settings import SettingsConfigDict  # добавить этот импорт

class OpenAISettings(BaseSettings):
    api_key: SecretStr = Field()
    
    model_config = SettingsConfigDict(env_file=".env")  # исправлено

if __name__ == "__main__":
    settings = OpenAISettings()  # исправлено
    print("Settings loaded successfully!")
    print(f"API key: {'*' * len(settings.api_key.get_secret_value())}")