from src.utils.common_logger import LOGGER


class BaseError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        LOGGER.error(message)

    def __str__(self) -> str:
        return self.message


class ConfigError(BaseError):
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message, status_code)


class RedisError(BaseError):
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message, status_code)


class MongoError(BaseError):
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message, status_code)
