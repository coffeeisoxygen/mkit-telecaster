"""application environtments setup."""

from enum import StrEnum

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class EnvironmentEnums(StrEnum):
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"


class ConfigEnvironment(BaseSettings):
    """Application Environment Setup."""

    environment: EnvironmentEnums = EnvironmentEnums.PRODUCTION
    name: str = "MKIT_WRAPPER"
    version: str = "0.1.0"
    debug: bool = False

    @field_validator("environment", mode="before")
    @classmethod
    def normalize_env(cls, v: str) -> str:
        if isinstance(v, str):
            v = v.upper()
        return v


class ConfigDatabase(BaseSettings):
    """Konfigurasi database untuk aplikasi."""

    url: str = "sqlite+aiosqlite:///./mkitparser.db"
    echo: bool = Field(
        False, description="Aktifkan logging SQL. Nonaktifkan untuk produksi."
    )

    timeout: int = Field(5, description="Waktu tunggu (detik) untuk koneksi database.")

    pool_size: int = Field(5, description="Jumlah koneksi yang disimpan dalam pool.")
    max_overflow: int = Field(
        10, description="Jumlah koneksi tambahan yang diizinkan saat pool penuh."
    )


class ConfigBotTelegram(BaseSettings):
    token: str
    chatid: str
