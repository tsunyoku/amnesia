from typing import Generic
from typing import TypeVar

import orjson
from aioredis import Redis

T = TypeVar("T")


class RedisCache(Generic[T]):
    def __init__(self, connection: Redis, identifier: str) -> None:
        self.connection = connection
        self.identifier = identifier

    async def get(self, key: str) -> T | None:
        value = await self.connection.hget(self.identifier, key)
        if value is None:
            return None

        return orjson.loads(value)

    async def set(self, key: str, value: T) -> None:
        raw_value = orjson.dumps(value)
        await self.connection.hset(self.identifier, key, raw_value)
