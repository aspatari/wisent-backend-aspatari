from common.application import BaseApplication
from .handlers import MessageHandler


class SocketApplication(BaseApplication):
    handlers = [MessageHandler]
    models_path = "model"
