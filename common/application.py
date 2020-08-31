from typing import List, Optional


class BaseApplication:
    handlers: List
    models_path: Optional[str] = None

    @classmethod
    def get_routes(cls):
        return [[handler.route, handler] for handler in cls.handlers]
