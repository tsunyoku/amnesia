from __future__ import annotations

from starlette.config import Config

cfg = Config()

LOG_LEVEL: int = cfg("LOG_LEVEL", cast=int)
