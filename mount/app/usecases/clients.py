from typing import Any

from app.common.context import Context
from app.models.client import OAuthClient
from app.models.status import Status
from app.repositories.clients import ClientsRepository
from app.usecases import cryptography as cryptography_usecases


async def fetch_one(
    ctx: Context,
    id: int | None = None,
    user_id: int | None = None,
    name: str | None = None,
    secret: str | None = None,
    status: Status = Status.ACTIVE,
) -> OAuthClient | None:
    repo = ClientsRepository(ctx)
    raw_client = await repo.fetch_one(
        id,
        user_id,
        name,
        secret,
        status,
    )
    if raw_client is None:
        return None

    return OAuthClient.parse_obj(raw_client)


async def fetch_all(
    ctx: Context,
    id: int | None = None,
    user_id: int | None = None,
    name: str | None = None,
    secret: str | None = None,
    status: Status = Status.ACTIVE,
) -> list[OAuthClient]:
    repo = ClientsRepository(ctx)
    raw_clients = await repo.fetch_all(
        id,
        user_id,
        name,
        secret,
        status,
    )

    return [OAuthClient.parse_obj(raw_client) for raw_client in raw_clients]


async def create_one(
    ctx: Context,
    user_id: int,
    name: str,
) -> OAuthClient:
    secret = cryptography_usecases.generate_secret()

    repo = ClientsRepository(ctx)
    raw_client = await repo.create_one(
        user_id,
        name,
        secret,
    )

    return OAuthClient.parse_obj(raw_client)


async def partial_update(
    ctx: Context,
    id: int,
    **updates: Any,
) -> OAuthClient:
    repo = ClientsRepository(ctx)
    raw_client = await repo.partial_update(
        id,
        **updates,
    )

    return OAuthClient.parse_obj(raw_client)


async def delete_one(ctx: Context, id: int) -> OAuthClient:
    repo = ClientsRepository(ctx)
    raw_client = await repo.delete_one(id)

    return OAuthClient.parse_obj(raw_client)
