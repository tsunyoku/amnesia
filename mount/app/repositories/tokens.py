from typing import Any

import orjson
from app.common.context import Context
from app.models.scope import Scope
from app.models.status import Status


class TokensRepository:
    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

        self.READ_PARAMS = (
            "id, user_id, client_id, token, refresh_token, scopes, status, created_at, "
            "updated_at, expires_at, deleted_at"
        )

    async def fetch_one(
        self,
        id: int | None = None,
        user_id: int | None = None,
        client_id: int | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        status: Status = Status.ACTIVE,
    ) -> dict[str, Any] | None:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM oauth_access_tokens
            WHERE
              id = COALESCE(:id, id)
              AND user_id = COALESCE(:user_id, user_id)
              AND client_id = COALESCE(:client_id, client_id)
              AND token = COALESCE(:token, token)
              AND refresh_token = COALESCE(:refresh_token, refresh_token)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "user_id": user_id,
            "client_id": client_id,
            "token": access_token,
            "refresh_token": refresh_token,
            "status": status,
        }

        token = await self.ctx.database.fetch_one(query, params)
        return token

    async def fetch_all(
        self,
        id: int | None = None,
        user_id: int | None = None,
        client_id: int | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        status: Status = Status.ACTIVE,
    ) -> list[dict[str, Any]]:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM oauth_access_tokens
            WHERE
              id = COALESCE(:id, id)
              AND user_id = COALESCE(:user_id, user_id)
              AND client_id = COALESCE(:client_id, client_id)
              AND token = COALESCE(:token, token)
              AND refresh_token = COALESCE(:refresh_token, refresh_token)
              AND status = COALESCE(:status, status)
        """
        params = {
            "id": id,
            "user_id": user_id,
            "client_id": client_id,
            "token": access_token,
            "refresh_token": refresh_token,
            "status": status,
        }

        tokens = await self.ctx.database.fetch_all(query, params)
        return tokens

    async def create_one(
        self,
        user_id: int,
        client_id: int,
        access_token: str,
        refresh_token: str | None,
        scopes: list[Scope],
    ) -> dict[str, Any]:
        query = f"""\
            INSERT INTO oauth_access_tokens (user_id, client_id, token, refresh_token, scopes)
            VALUES (:user_id, :client_id, :token, :refresh_token, :scopes)
        """
        params = {
            "user_id": user_id,
            "client_id": client_id,
            "token": access_token,
            "refresh_token": refresh_token,
            "scopes": orjson.dumps(scopes),
        }

        await self.ctx.database.execute(query, params)
        token = await self.fetch_one(access_token=access_token)
        assert token is not None
        return token

    async def partial_update(
        self,
        id: int,
        **updates: Any,
    ) -> dict[str, Any]:
        query = f"""\
            UPDATE oauth_access_tokens
            SET {", ".join(f"{k} = :{k}" for k in updates)}
            WHERE id = :id
        """
        params = {
            "id": id,
            **updates,
        }

        await self.ctx.database.execute(query, params)
        token = await self.fetch_one(id=id)
        assert token is not None
        return token

    async def delete_one(self, id: int) -> dict[str, Any]:
        query = f"""\
            UPDATE oauth_access_tokens
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
        token = await self.fetch_one(id=id, status=Status.DELETED)
        assert token is not None
        return token
