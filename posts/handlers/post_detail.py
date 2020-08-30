from tornado.ioloop import IOLoop

from common.handler import BaseJsonRequestHandler
from core.application import App
from ..service import get_post_by_id, PostNotFound


@App.add_handler
class PostDetailAsync(BaseJsonRequestHandler):
    route = "/v1/posts/(?P<post_id>\d+)"

    async def get(self, post_id: int):
        try:
            post = await IOLoop.current().run_in_executor(None, get_post_by_id, post_id)
            self.success(post)

        except Exception as e:
            from devtools import debug
            debug(e)
            self.error(e)
