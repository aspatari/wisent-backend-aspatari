from common.application import BaseApplication
from .handlers import ClientListCreateHandler, ClientCreateEditDelete


class ClientApplication(BaseApplication):
    handlers = [ClientListCreateHandler, ClientCreateEditDelete]
    models_path = "model"
