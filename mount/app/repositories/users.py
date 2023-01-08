from typing import Any

from app.common.context import Context
from app.models.status import Status


class UsersRepository:
    def __init__(self, ctx: Context):
        self.ctx = ctx

        self.READ_PARAMS = (
            "id, username, email, country_acronym, bcrypt_password, privileges, "
            "default_mode, friend_only_dms, show_status, last_visit, restricted_at, supporter_until, "
            "userpage_bbcode, default_group, status, created_at, updated_at, deleted_at"
        )

    async def fetch_one(
        self,
        id: int | None = None,
        username: str | None = None,
        email: str | None = None,
        status: Status | None = Status.ACTIVE,
    ) -> dict[str, Any] | None:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM users
            WHERE
              id = COALESCE(:id, id)
              AND username = COALESCE(:username, username)
              AND email = COALESCE(:email, email)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "username": username,
            "email": email,
            "status": status,
        }

        user = await self.ctx.database.fetch_one(query, params)
        return user

    async def fetch_all(
        self,
        id: int | None = None,
        username: str | None = None,
        email: str | None = None,
        status: Status = Status.ACTIVE,
    ) -> list[dict[str, Any]]:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM users
            WHERE
              id = COALESCE(:id, id)
              AND username = COALESCE(:username, username)
              AND email = COALESCE(:email, email)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "username": username,
            "email": email,
            "status": status,
        }

        users = await self.ctx.database.fetch_all(query, params)
        return users

    async def create_one(
        self,
        username: str,
        email: str,
        country_acronym: str,
        bcrypt_password: str,
    ) -> dict[str, Any]:
        query = """\
            INSERT INTO users (username, email, country_acronym, bcrypt_password)
            VALUES (:username, :email, :country_acronym, :bcrypt_password)
        """
        params = {
            "username": username,
            "email": email,
            "country_acronym": country_acronym,
            "bcrypt_password": bcrypt_password,
        }

        await self.ctx.database.execute(query, params)
        user = await self.fetch_one(username=username)
        assert user is not None
        return user

    async def partial_update(
        self,
        id: int,
        **updates: Any,
    ) -> dict[str, Any]:
        query = f"""\
            UPDATE users
            SET {", ".join(f"{k} = :{k}" for k in updates)}
            WHERE id = :id
        """
        params = {
            "id": id,
            **updates,
        }

        await self.ctx.database.execute(query, params)
        user = await self.fetch_one(id=id)
        assert user is not None

        return user

    async def delete_one(
        self,
        id: int,
    ) -> dict[str, Any]:
        query = """\
            UPDATE users
            SET
              status = :status
              AND deleted_at = CURRENT_TIMESTAMP()
            WHERE
              id = :id
        """
        params = {
            "id": id,
            "status": Status.DELETED,
        }

        await self.ctx.database.execute(query, params)
        user = await self.fetch_one(id=id, status=Status.DELETED)
        assert user is not None
        return user
