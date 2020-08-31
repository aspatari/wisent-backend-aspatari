from typing import Type

from tornado.util import import_object
from tornado.web import Application
import logging
from common.application import BaseApplication
from common.handler import BaseJsonRequestHandler

logger = logging.getLogger("app")


class App(Application):
    apps = ["apps.posts", 'apps.clients', "apps.socket"]
    handlers = []
    models = []

    def __init__(self):
        settings = {"debug": True}
        self.load_applications()
        super(App, self).__init__(handlers=self.handlers, **settings)

    def load_applications(self):
        for app in self.apps:
            module = import_object(app)
            application = module.application
            application_class: Type[BaseApplication] = import_object(f"{app}.{application}")
            routes = application_class().get_routes()
            if routes:
                from devtools import debug
                self.handlers.extend(routes)
            if application_class.models_path is not None:
                self.models.append(f"{app}.{application_class.models_path}")
