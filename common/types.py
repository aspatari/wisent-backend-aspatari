from typing import Union
from uuid import UUID

ID = Union[UUID, 'str']


class Empty:
    ...


empty = Empty()
