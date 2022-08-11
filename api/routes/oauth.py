from __future__ import annotations

from typing import Literal

from fastapi import Form
from fastapi import status
from fastapi.responses import ORJSONResponse

import repositories.users
import usecases.passwords
from api import responses
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
    assert client_secret == "FGc9GAtyHzeQDshWP5Ah7dega8hJACAJpQtw6OXk"

    # TODO: what is osu!'s error responses?

    user = await repositories.users.fetch_by_name(username)
    if not user:
        return responses.error(
            status.HTTP_401_UNAUTHORIZED,
            "incorrect username/password",
        )

    if not await usecases.passwords.verify(password, user.password_bcrypt):
        return responses.error(
            status.HTTP_401_UNAUTHORIZED,
            "incorrect username/password",
        )

    return responses.success(
        {
            "token_type": "Bearer",
            "expires_in": 0,
            "access_token": "",
            "refresh_token": "",
        },
    )
