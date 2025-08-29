from app.exception import AppExceptionError


class InternalServiceError(AppExceptionError):
    """Exception raised for internal server errors."""

    status_code = 500
    default_message = "Internal Server Error"
