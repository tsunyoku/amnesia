from __future__ import annotations

from typing import Any
from typing import Literal

from fastapi import Form
from fastapi import status
from fastapi.responses import ORJSONResponse

import repositories.sessions
import repositories.users
import usecases.passwords
from api.routes import router


@router.post("/oauth/token")
async def oauth_token(
    username: str = Form(...),
    password: str = Form(...),
    grant_type: Literal["password"] = Form(...),
    client_id: int = Form(...),
    client_secret: str = Form(...),
    scope: Literal["*"] = Form(...),
) -> ORJSONResponse:
    # osu!lazer has a static id and secret
    assert client_id == 5
    assert client_secret in (
        "FGc9GAtyHzeQDshWP5Ah7dega8hJACAJpQtw6OXk",  # production
        "3LP2mhUrV89xxzD1YKNndXHEhWWCRLPNKioZ9ymT",  # development
    )

    # TODO: what is osu!'s error responses?

    user = await repositories.users.fetch_by_name(username)
    if not user:
        return ORJSONResponse(
            content="incorrect username/password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    if not await usecases.passwords.verify(password, user.password_bcrypt):
        return ORJSONResponse(
            content="incorrect username/password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    session = await repositories.sessions.create(user.id)

    return ORJSONResponse(
        content={
            "token_type": "Bearer",
            "expires_in": session.expires_in.total_seconds(),
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
        },
    )
