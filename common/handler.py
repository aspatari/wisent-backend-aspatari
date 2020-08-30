from tornado.escape import json_encode
from tornado.web import RequestHandler, HTTPError


class BaseJsonRequestHandler(RequestHandler):
    route: str

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def return_json(self, data):
        self.finish(json_encode(data))

    def success(self, data):
        return self.return_json(data=data)

    def error(self, exception: HTTPError):
        self.write({'status': exception.status_code, 'message': exception.log_message})
        self.set_status(exception.status_code)
        self.finish()
