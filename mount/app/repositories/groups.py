from typing import Any

from app.common.context import Context


class GroupsRepository:
    def __init__(self, ctx: Context):
        self.ctx = ctx

        self.READ_PARAMS = "id, identifier, name, short_name, description_markdown, playmodes, colour, leader_id"

    async def fetch_one(
        self,
        id: int | None = None,
        identifier: str | None = None,
        name: str | None = None,
        short_name: str | None = None,
        leader_id: int | None = None,
    ) -> dict[str, Any] | None:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM groups
            WHERE
              id = COALESCE(:id, id)
              AND identifier = COALESCE(:identifier, identifier)
              AND name = COALESCE(:name, name)
              AND short_name = COALESCE(:short_name, short_name)
              AND leader_id = COALESCE(:leader_id, leader_id)
        """
        params = {
            "id": id,
            "identifier": identifier,
            "name": name,
            "short_name": short_name,
            "leader_id": leader_id,
        }

        group = await self.ctx.database.fetch_one(query, params)
        return group

    async def fetch_all(
        self,
        id: int | None = None,
        identifier: str | None = None,
        name: str | None = None,
        short_name: str | None = None,
        leader_id: int | None = None,
    ) -> list[dict[str, Any]]:
        query = f"""\
            SELECT {self.READ_PARAMS}
            FROM groups
            WHERE
              id = COALESCE(:id, id)
              AND identifier = COALESCE(:identifier, identifier)
              AND name = COALESCE(:name, name)
              AND short_name = COALESCE(:short_name, short_name)
              AND leader_id = COALESCE(:leader_id, leader_id)
        """
        params = {
            "id": id,
            "identifier": identifier,
            "name": name,
            "short_name": short_name,
            "leader_id": leader_id,
        }

        groups = await self.ctx.database.fetch_all(query, params)
        return groups

    async def create_one(
        self,
        identifier: str,
        name: str,
        short_name: str,
        leader_id: int,
        description_markdown: str | None = None,
        playmodes: list[str] | None = None,
        colour: str | None = None,
    ) -> dict[str, Any]:
        query = f"""\
            INSERT INTO groups (identifier, name, short_name, description_markdown, playmodes, colour, leader_id)
            VALUES (:identifier, :name, :short_name, :description_markdown, :playmodes, :colour, :leader_id)
        """
        params = {
            "identifier": identifier,
            "name": name,
            "short_name": short_name,
            "description_markdown": description_markdown,
            "playmodes": playmodes,
            "colour": colour,
            "leader_id": leader_id,
        }

        await self.ctx.database.execute(query, params)
        group = await self.fetch_one(identifier=identifier)
        assert group is not None
        return group
