from aioredis import Redis
from app.models.redis_cache import RedisCache
from asyncql import Database
from fastapi import Request
from geoip2.database import Reader


class Context:
    def __init__(self, request: Request) -> None:
        self.request = request

    @property
    def database(self) -> Database:
        return self.request.app.state.database

    @property
    def redis(self) -> Redis:
        return self.request.app.state.redis

    @property
    def bcrypt_cache(self) -> RedisCache[str]:
        return self.request.app.state.bcrypt_cache

    @property
    def geolocation_reader(self) -> Reader:
        return self.request.app.state.geolocation_reader
