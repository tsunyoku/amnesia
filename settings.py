from __future__ import annotations

from starlette.config import Config

cfg = Config()

LOG_LEVEL: int = cfg("LOG_LEVEL", cast=int)

READ_DB_USER: str = cfg("READ_DB_USER")
READ_DB_PASS: str = cfg("READ_DB_PASS")
READ_DB_HOST: str = cfg("READ_DB_HOST")
READ_DB_PORT: int = cfg("READ_DB_PORT", cast=int)
READ_DB_NAME: str = cfg("READ_DB_NAME")
READ_DB_DSN = "mysql://{}:{}@{}:{}/{}".format(
    READ_DB_USER,
    READ_DB_PASS,
    READ_DB_HOST,
    READ_DB_PORT,
    READ_DB_NAME,
)

WRITE_DB_USER: str = cfg("WRITE_DB_USER")
WRITE_DB_PASS: str = cfg("WRITE_DB_PASS")
WRITE_DB_HOST: str = cfg("WRITE_DB_HOST")
WRITE_DB_PORT: int = cfg("WRITE_DB_PORT", cast=int)
WRITE_DB_NAME: str = cfg("WRITE_DB_NAME")
WRITE_DB_DSN = "mysql://{}:{}@{}:{}/{}".format(
    WRITE_DB_USER,
    WRITE_DB_PASS,
    WRITE_DB_HOST,
    WRITE_DB_PORT,
    WRITE_DB_NAME,
)

REDIS_HOST: str = cfg("REDIS_HOST")
REDIS_PORT: int = cfg("REDIS_PORT", cast=int)
REDIS_DSN = "redis://{}:{}".format(REDIS_HOST, REDIS_PORT)
