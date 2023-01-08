from typing import Any

from app.common.context import Context
from app.models.status import Status


class ClientsRepository:
    def __init__(self, ctx: Context):
        self.ctx = ctx

        self.READ_PARAMS = (
            "id, user_id, name, secret, status, created_at, updated_at, deleted_at"
        )

    async def fetch_one(
        self,
        id: int | None = None,
        user_id: int | None = None,
        name: str | None = None,
        secret: str | None = None,
        status: Status = Status.ACTIVE,
    ) -> dict[str, Any] | None:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM oauth_clients
            WHERE
              id = COALESCE(:id, id)
              AND user_id = COALESCE(:user_id, user_id)
              AND name = COALESCE(:name, name)
              AND secret = COALESCE(:secret, secret)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "user_id": user_id,
            "name": name,
            "secret": secret,
            "status": status,
        }

        client = await self.ctx.database.fetch_one(query, params)
        return client

    async def fetch_all(
        self,
        id: int | None = None,
        user_id: int | None = None,
        name: str | None = None,
        secret: str | None = None,
        status: Status = Status.ACTIVE,
    ) -> list[dict[str, Any]]:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM oauth_clients
            WHERE
              id = COALESCE(:id, id)
              AND user_id = COALESCE(:user_id, user_id)
              AND name = COALESCE(:name, name)
              AND secret = COALESCE(:secret, secret)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "user_id": user_id,
            "name": name,
            "secret": secret,
            "status": status,
        }

        clients = await self.ctx.database.fetch_all(query, params)
        return clients

    async def create_one(
        self,
        user_id: int,
        name: str,
        secret: str,
    ) -> dict[str, Any]:
        query = f"""\
            INSERT INTO oauth_clients (user_id, name, secret)
            VALUES (:user_id, :name, :secret)
        """
        params = {
            "user_id": user_id,
            "name": name,
            "secret": secret,
        }

        await self.ctx.database.execute(query, params)
        client = await self.fetch_one(secret=secret)
        assert client is not None

        return client

    async def partial_update(
        self,
        id: int,
        **updates: Any,
    ) -> dict[str, Any]:
        query = f"""\
            UPDATE oauth_clients
            SET {", ".join(f"{k} = :{k}" for k in updates)}
            WHERE id = :id
        """
        params = {
            "id": id,
            **updates,
        }

        await self.ctx.database.execute(query, params)
        client = await self.fetch_one(id=id)
        assert client is not None

        return client

    async def delete_one(self, id: int) -> dict[str, Any]:
        query = f"""\
            UPDATE oauth_clients
            SET
              status = :status,
              deleted_at = CURRENT_TIMESTAMP()
            WHERE
              id = :id
        """
        params = {
            "id": id,
            "status": Status.DELETED,
        }

        await self.ctx.database.execute(query, params)
        client = await self.fetch_one(id=id, status=Status.DELETED)
        assert client is not None
        return client
