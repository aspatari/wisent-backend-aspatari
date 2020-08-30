from typing import TypedDict, List, Union, Type
from tornado.httpclient import (
    HTTPClient,
    HTTPRequest,
    AsyncHTTPClient,
    HTTPClientError,
)
from tornado.escape import json_decode
from tornado.web import HTTPError

from posts.exceptions import PostNotFound


class Post(TypedDict):
    userId: int
    id: int
    title: str
    body: str


BASE_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_posts(*, client: AsyncHTTPClient = AsyncHTTPClient()) -> List[Post]:
    """Retrieve posts from fake api"""
    request = HTTPRequest(url=BASE_URL, method="GET", validate_cert=False)
    response = await client.fetch(request)
    posts = json_decode(response.body)
    return posts


def get_post_by_id(
    post_id: int, *, client: HTTPClient = HTTPClient()
) -> Union[Post, HTTPError]:
    """Retrieve post by id from fake api"""
    url = f"{BASE_URL}/{post_id}"
    request = HTTPRequest(url=url, method="GET", validate_cert=False)
    try:
        response = client.fetch(request)
        post = json_decode(response.body)
        return post
    except HTTPClientError as e:
        if e.code == 404:
            raise PostNotFound(status_code=404, log_message=f"Post with {post_id} not found")
        else:
            raise HTTPError(status_code=e.code, log_message=e.message)
