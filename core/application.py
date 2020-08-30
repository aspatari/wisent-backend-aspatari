from typing import Type

from tornado.web import Application
import logging

from common.handler import BaseJsonRequestHandler

logger = logging.getLogger("app")


class App(Application):
    handlers = []

    def __init__(self):
        settings = {"debug": True}
        from posts import handlers
        super(App, self).__init__(handlers=self.handlers, **settings)

    @classmethod
    def add_handler(cls, hanlder: Type[BaseJsonRequestHandler]):
        cls.handlers.append([hanlder.route, hanlder])
        logger.info(f"Register Handler in path {hanlder.route}")
        from devtools import debug
        debug(f"Register Handler in path {hanlder.route}")

        return hanlder
