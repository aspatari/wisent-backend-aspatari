import asyncio

import tornado.httpserver as httpserver
import uvloop

from .application import App


def run_server(port=8000):
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = App()
    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(port)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    run_server()
