from tornado.web import HTTPError


class PostNotFound(HTTPError):
    status_code = 404
