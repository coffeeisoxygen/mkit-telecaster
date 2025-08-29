"""schemas for telegram bot."""

import re
from datetime import datetime

from pydantic import BaseModel, field_validator


class BotConfigCreate(BaseModel):
    token: str
    name: str | None = None
    description: str | None = None
    is_active: bool = True

    @field_validator("token")
    @classmethod
    def validate_token(cls, values: str) -> str:
        # Basic telegram bot token format validation
        # Format: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
        pattern = r"^\d+:[A-Za-z0-9_-]+$"
        if not re.match(pattern, values):
            raise ValueError("Invalid telegram bot token format")
        return values


class BotConfigUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class BotConfigResponse(BaseModel):
    id: int
    token: str
    name: str | None
    description: str | None
    is_active: bool
    is_valid: bool
    bot_username: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class BotValidationResponse(BaseModel):
    is_valid: bool
    bot_info: dict | None = None
    error_message: str | None = None
