import databases
import aioredis
import httpx

database: databases.Database
redis: aioredis.Redis
http: httpx.AsyncClient


async def connect_services() -> None:
    ...


async def disconnect_services() -> None:
    ...
