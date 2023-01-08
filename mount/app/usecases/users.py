from typing import Any

from app.common.context import Context
from app.models.status import Status
from app.models.user import User
from app.repositories.users import UsersRepository


async def fetch_one(
    ctx: Context,
    id: int | None = None,
    username: str | None = None,
    email: str | None = None,
    status: Status | None = Status.ACTIVE,
) -> User | None:
    repo = UsersRepository(ctx)
    raw_user = await repo.fetch_one(
        id,
        username,
        email,
        status,
    )
    if raw_user is None:
        return None

    return User.parse_obj(raw_user)


async def fetch_all(
    ctx: Context,
    id: int | None = None,
    username: str | None = None,
    email: str | None = None,
    status: Status = Status.ACTIVE,
) -> list[User]:
    repo = UsersRepository(ctx)
    raw_users = await repo.fetch_all(
        id,
        username,
        email,
        status,
    )

    return [User.parse_obj(raw_user) for raw_user in raw_users]


async def create_one(
    ctx: Context,
    username: str,
    email: str,
    country_acronym: str,
    bcrypt_password: str,
) -> User:
    repo = UsersRepository(ctx)
    raw_user = await repo.create_one(
        username,
        email,
        country_acronym,
        bcrypt_password,
    )

    return User.parse_obj(raw_user)


async def partial_update(
    ctx: Context,
    id: int,
    **updates: Any,
) -> User:
    repo = UsersRepository(ctx)
    raw_user = await repo.partial_update(
        id,
        **updates,
    )

    return User.parse_obj(raw_user)


async def delete_one(ctx: Context, id: int) -> User:
    repo = UsersRepository(ctx)
    raw_user = await repo.delete_one(id)

    return User.parse_obj(raw_user)
