from common.handler import BaseJsonRequestHandler
from ..service import get_posts


class PostList(BaseJsonRequestHandler):
    route = "/v1/posts"

    async def get(self):
        posts = await get_posts()
        self.return_json(posts)
