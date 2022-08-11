from __future__ import annotations

from fastapi import FastAPI


def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        ...

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        ...


def init_api() -> FastAPI:
    app = FastAPI()

    init_events(app)

    return app


app = init_api()
