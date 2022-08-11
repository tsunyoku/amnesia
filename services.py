from objects.database import Database

import databases
import settings
import aioredis
import httpx

read_database: databases.Database
write_database: databases.Database
database: Database

redis: aioredis.Redis
http: httpx.AsyncClient


async def connect_services() -> None:
    global read_database, write_database, database, http, redis

    read_database = databases.Database(settings.READ_DB_DSN)
    write_database = databases.Database(settings.WRITE_DB_DSN)
    database = Database(read_database, write_database)

    redis = aioredis.from_url(settings.REDIS_DSN)

    await read_database.connect()
    await write_database.connect()
    await redis.initialize()


async def disconnect_services() -> None:
    global read_database, write_database, database, http, redis

    await read_database.disconnect()
    await write_database.disconnect()
    await redis.close()
