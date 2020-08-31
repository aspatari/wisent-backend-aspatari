from tornado.websocket import WebSocketHandler


class MessageHandler(WebSocketHandler):
    route = "/ws"

    def open(self):
        from devtools import debug
        debug("open")

    def on_close(self):
        from devtools import debug
        debug("close")

    async def on_message(self, message):
        from ..service import message_service
        await message_service.create_message(message=message)
