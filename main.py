import asyncio

import tornado.httpserver as httpserver
import uvloop
from tornado.ioloop import IOLoop
from tornado.locks import Event
from tornado.platform.asyncio import AsyncIOMainLoop

from core import settings
from core.application import App
from core.database import init_database


async def run_server(port=8000, address="0.0.0.0"):
    app = App(settings=settings.APP_SETTINGS)
    await init_database(db_url=settings.DATABASE_URL, models=app.models)
    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(port=settings.PORT, address=settings.ADDRESS)
    shutdown_event = Event()
    event = await shutdown_event.wait()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    AsyncIOMainLoop().install()

    IOLoop.current().run_sync(run_server)
