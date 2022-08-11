from __future__ import annotations

import logging

from fastapi import FastAPI

import services
from api.routes import router


def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        await services.connect_services()
        logging.info("Amnesia started")

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        await services.disconnect_services()
        logging.info("Amnesia stopped")


def init_api() -> FastAPI:
    app = FastAPI()

    init_events(app)
    app.include_router(router)

    return app


app = init_api()
