from tornado.web import HTTPError
from tortoise import Model

from common.types import ID


class TornadoValidationError(HTTPError):
    def __init__(
        self, status_code: int = 500, log_message: str = None, *args, **kwargs
    ) -> None:
        self.status_code = status_code
        self.log_message = log_message


class TornadoDoseNotExist(HTTPError):
    def __init__(self, id: ID, *args, **kwargs) -> None:
        self.status_code = 404
        self.log_message = f"Object with {id} Dose Not Exist"
