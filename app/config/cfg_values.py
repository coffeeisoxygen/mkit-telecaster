"""application environtments setup."""

from pydantic_settings import BaseSettings


class ConfigEnvironment(BaseSettings):
    environment: str = "production"
    debug: bool = False


class ConfigBotTelegram(BaseSettings):
    token: str
    chat_id: str
