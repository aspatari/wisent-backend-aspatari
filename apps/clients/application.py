from .handlers import ClientList, ClientCreate
from .model import Client
from common.application import BaseApplication


class ClientApplication(BaseApplication):
    handlers = [ClientList, ClientCreate]
    models_path = "model"
