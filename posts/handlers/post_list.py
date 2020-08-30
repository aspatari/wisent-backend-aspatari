from common.handler import BaseJsonRequestHandler
from core.application import App
from ..service import get_posts


@App.add_handler
class PostList(BaseJsonRequestHandler):
    route = "/v1/posts"

    async def get(self):
        posts = await get_posts()
        self.return_json(posts)
