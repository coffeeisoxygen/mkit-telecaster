from app.exception import AppExceptionError


class InternalServiceError(AppExceptionError):
    """Exception raised for internal server errors."""

    status_code = 500
    default_message = "Internal Server Error"


class TeleBotGenericError(AppExceptionError):
    """Exception raised for Telegram Bot errors."""

    status_code = 400
    default_message = "Telegram Bot Error"


class TeleBotNotFoundError(TeleBotGenericError):
    """Exception raised for BotService errors."""

    status_code = 404
    default_message = "Telegram Bot Not Found"


class TeleBotInvalidTokenError(TeleBotGenericError):
    """Exception raised for invalid bot token errors."""

    status_code = 401
    default_message = "Telegram Bot Invalid Token"


class TeleChannelNotFoundError(TeleBotGenericError):
    """Exception raised for Telegram channel not found errors."""

    status_code = 404
    default_message = "Telegram Channel Not Found"
