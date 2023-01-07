import aioredis
from app.common import logger
from app.common import settings
from app.models.redis_cache import RedisCache
from asyncql import Database
from fastapi import FastAPI
from geoip2.database import Reader


def mysql_dsn(username: str, password: str, host: str, port: int, database: str) -> str:
    return f"mysql://{username}:{password}@{host}:{port}/{database}"


def init_db(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup_database() -> None:
        logger.info("Connecting to database")

        database = Database(
            mysql_dsn(
                username=settings.DB_USER,
                password=settings.DB_PASS,
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                database=settings.DB_NAME,
            ),
        )
        await database.connect()

        app.state.database = database
        logger.info("Connected to database")

    @app.on_event("shutdown")
    async def shutdown_database() -> None:
        logger.info("Disconnecting from database")

        await app.state.database.disconnect()
        del app.state.database

        logger.info("Disconnected from database")


def init_redis(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup_redis() -> None:
        logger.info("Connecting to redis")

        redis = aioredis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
        )
        await redis.initialize()

        app.state.redis = redis
        logger.info("Connected to redis")

    @app.on_event("shutdown")
    async def shutdown_redis() -> None:
        logger.info("Disconnecting from redis")

        await app.state.redis.close()
        del app.state.redis

        logger.info("Disconnected from redis")


def init_bcrypt_cache(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup_bcrypt_cache() -> None:
        logger.info("Initializing bcrypt cache")

        bcrypt_cache: RedisCache[str] = RedisCache(
            app.state.redis,
            "amnesia:cache:bcrypt",
        )
        app.state.bcrypt_cache = bcrypt_cache

        logger.info("Initialized bcrypt cache")

    @app.on_event("shutdown")
    async def shutdown_bcrypt_cache() -> None:
        logger.info("Destroying bcrypt cache")

        del app.state.bcrypt_cache

        logger.info("Destroyed bcrypt cache")


def init_geolocation_reader(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup_geolocation_reader() -> None:
        logger.info("Initializing geolocation reader")

        geolocation_reader = Reader(settings.GEOLOCATION_DB_PATH)
        app.state.geolocation_reader = geolocation_reader

        logger.info("Initialized geolocation reader")


def init_routes(app: FastAPI) -> None:
    ...


def init_api() -> FastAPI:
    app = FastAPI()

    init_db(app)
    init_redis(app)
    init_bcrypt_cache(app)
    init_geolocation_reader(app)
    init_routes(app)

    return app
