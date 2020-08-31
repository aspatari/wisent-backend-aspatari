from tornado.web import HTTPError


class TornadoValidationError(HTTPError):

    def __init__(
        self, status_code: int = 500, log_message: str = None, *args, **kwargs
    ) -> None:
        self.status_code = status_code
        self.log_message = log_message

