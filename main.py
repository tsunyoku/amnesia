#!/usr/bin/env python3.10
from __future__ import annotations

import logging

import uvicorn
import uvloop

import settings

uvloop.install()

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s %(message)s",
)


def main() -> int:
    uvicorn.run(
        "api.init_api:app",
        reload=settings.LOG_LEVEL == 10,  # log level 10 == debug
        log_level=settings.LOG_LEVEL,  # type: ignore
        server_header=False,
        date_header=False,
        host="0.0.0.0",
        port=80,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
