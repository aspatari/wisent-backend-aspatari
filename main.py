import asyncio

import tornado
import tornado.httpserver as httpserver
import uvloop
from tornado.ioloop import IOLoop
from tornado.locks import Event
from tornado.options import define, options
from tornado.platform.asyncio import AsyncIOMainLoop

from core.database import init_database

from core.application import App

define("port", default=8000, help="run on the given port", type=int)
define("address", default="0.0.0.0", help="address that server will listen", type=str)
define("db_url", default="postgres://postgres:artemir@localhost:5432/wisent", help="Database connection url", type=str)

options.parse_command_line()


async def run_server(port=8000, address="0.0.0.0"):
    app = App()
    await init_database(db_url=options.db_url, models=app.models)
    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(port=port, address=address)
    shutdown_event = Event()
    event = await shutdown_event.wait()
    print(event)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    AsyncIOMainLoop().install()

    IOLoop.current().run_sync(run_server)
