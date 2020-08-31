from typing import TypedDict, List, Optional

from tornado.escape import json_decode
from tornado.httpclient import (
    HTTPClient,
    HTTPRequest,
    AsyncHTTPClient,
    HTTPClientError,
)
from tornado.web import HTTPError

from .exceptions import PostNotFound


class Post(TypedDict):
    userId: int
    id: int
    title: str
    body: str


BASE_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_posts(*, client: Optional[AsyncHTTPClient] = None, url=BASE_URL) -> List[Post]:
    """
    Retrieve posts from fake api
    :arg client: HTTPClient exposed like argument for mocking for tests
    :arg url: Base URL for post api

    """
    request = HTTPRequest(url=url, method="GET", validate_cert=False)
    try:
        if client is None:
            client = AsyncHTTPClient()
        response = await client.fetch(request)
        posts = json_decode(response.body)
        return posts
    except HTTPClientError as e:
        raise HTTPError(status_code=e.code, log_message=e.message)


def get_post_by_id(post_id: int, *, client: Optional[HTTPClient] = None, url=BASE_URL) -> Post:
    """
    Retrieve post by id
    :arg post_id: Post ID
    :arg client: HTTPClient exposed like argument for mocking for tests
    :arg url: Base URL for post api

    """
    url = f"{url}/{post_id}"
    request = HTTPRequest(url=url, method="GET", validate_cert=False)
    # import time; time.sleep(5) # uncomment this for testing blocking mode
    try:
        if client is None:
            client = HTTPClient()
        response = client.fetch(request)
        post = json_decode(response.body)
        return post
    except HTTPClientError as e:
        if e.code == 404:
            raise PostNotFound(
                status_code=404, log_message=f"Post with {post_id} not found"
            )
        else:
            raise HTTPError(status_code=e.code, log_message=e.message)
