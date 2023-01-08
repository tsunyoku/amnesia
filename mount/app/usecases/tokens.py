from typing import Any

from app.common.context import Context
from app.models.scope import Scope
from app.models.status import Status
from app.models.token import OAuthToken
from app.repositories.tokens import TokensRepository
from app.usecases import cryptography as cryptography_usecases


async def fetch_one(
    ctx: Context,
    id: int | None = None,
    user_id: int | None = None,
    client_id: int | None = None,
    access_token: str | None = None,
    refresh_token: str | None = None,
    status: Status = Status.ACTIVE,
) -> OAuthToken | None:
    repo = TokensRepository(ctx)
    raw_token = await repo.fetch_one(
        id,
        user_id,
        client_id,
        access_token,
        refresh_token,
        status,
    )
    if raw_token is None:
        return None

    return OAuthToken.parse_obj(raw_token)


async def fetch_all(
    ctx: Context,
    id: int | None = None,
    user_id: int | None = None,
    client_id: int | None = None,
    access_token: str | None = None,
    refresh_token: str | None = None,
    status: Status = Status.ACTIVE,
) -> list[OAuthToken]:
    repo = TokensRepository(ctx)
    raw_tokens = await repo.fetch_all(
        id,
        user_id,
        client_id,
        access_token,
        refresh_token,
        status,
    )

    return [OAuthToken.parse_obj(raw_token) for raw_token in raw_tokens]


async def create_one(
    ctx: Context,
    user_id: int,
    client_id: int,
    scopes: list[Scope],
) -> OAuthToken:
    # only lazer needs refresh token
    if client_id == 5 and Scope.ALL in scopes:
        # osu uses 993
        refresh_token = cryptography_usecases.generate_secret(length=1_000)
    else:
        refresh_token = None

    # osu uses 993
    access_token = cryptography_usecases.generate_secret(length=1_000)

    repo = TokensRepository(ctx)
    raw_token = await repo.create_one(
        user_id,
        client_id,
        access_token,
        refresh_token,
        scopes,
    )

    return OAuthToken.parse_obj(raw_token)


async def partial_update(
    ctx: Context,
    id: int,
    **updates: Any,
) -> OAuthToken:
    repo = TokensRepository(ctx)
    raw_token = await repo.partial_update(
        id,
        **updates,
    )

    return OAuthToken.parse_obj(raw_token)


async def delete_one(
    ctx: Context,
    id: int,
) -> OAuthToken:
    repo = TokensRepository(ctx)
    raw_token = await repo.delete_one(id)

    return OAuthToken.parse_obj(raw_token)
