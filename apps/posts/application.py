from .handlers import PostDetailAsync, PostList
from common.application import BaseApplication


class PostApplication(BaseApplication):
    handlers = [PostDetailAsync, PostList]
