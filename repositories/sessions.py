from __future__ import annotations

import secrets
from datetime import datetime
from datetime import timedelta

import orjson

import services
from models.session import Session


async def create(user_id: int) -> Session:
    session = Session(
        id=user_id,
        token_type="Bearer",
        access_token=secrets.token_urlsafe(32),
        token_expiry=datetime.utcnow() + timedelta(hours=24),
        refresh_token=secrets.token_urlsafe(32),
    )

    await services.redis.setex(
        name=f"amnesia:sessions:{session.access_token}",
        time=timedelta(hours=24),
        value=orjson.dumps(session.dict()),
    )

    return session
