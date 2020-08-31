import logging
from typing import Type

from tornado.util import import_object
from tornado.web import Application

from common.application import BaseApplication

logger = logging.getLogger("app")


class App(Application):
    apps = ["apps.posts", "apps.clients", "apps.socket"]
    handlers = []
    models = []

    def __init__(self, settings):

        self.load_applications()
        super(App, self).__init__(handlers=self.handlers, **settings)

    def load_applications(self):
        for app in self.apps:
            try:
                module = import_object(app)
                application = module.application
                logger.info(f"[Load Module][{app}]")
                application_class: Type[BaseApplication] = import_object(
                    f"{app}.{application}"
                )
                logger.info(f"[Load Application Class][{application_class}]")
                routes = application_class().get_routes()
                if routes:
                    for route in routes:
                        self.handlers.append(route)
                        logger.info(f"[Add handler][{route[0]}][{route[1]}]")
                if application_class.models_path is not None:
                    model_path = f"{app}.{application_class.models_path}"
                    self.models.append(model_path)
                    logger.info(f"[Load Model][{model_path}]")
            except ImportError:
                logger.exception(f"Can't log  {app}")
