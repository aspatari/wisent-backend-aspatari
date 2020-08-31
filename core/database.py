from typing import List

from tortoise import Tortoise


async def init_database(db_url: str, models: List[str]):
    await Tortoise.init(
        db_url=db_url,
        modules={'models': models}
    )
    await Tortoise.generate_schemas()
