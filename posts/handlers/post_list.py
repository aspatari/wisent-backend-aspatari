from common.handler import BaseRequestHandler
from core.application import App
from ..service import get_posts


@App.add_handler
class PostList(BaseRequestHandler):
    route = "/v1/posts"

    async def get(self):
        posts = await get_posts()
        self.return_json(posts)
