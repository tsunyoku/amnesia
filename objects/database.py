from databases.interfaces import Record
from typing import Any

import databases


class Database:
    """
    This class aims to automatically manage the usage
    of having a separate read and write database  connection
    by providing a thin wrapper of databases which calls the read or write database
    depending on the operation.
    """

    def __init__(
        self,
        read_database: databases.Database,
        write_database: databases.Database,
    ) -> None:
        self.read_database = read_database
        self.write_database = write_database

    async def _ensure_connection(self) -> None:
        for database in (
            self.read_database,
            self.write_database,
        ):
            if not database.is_connected:
                await database.connect()

    async def fetch_val(
        self,
        query: str,
        mapping: dict | None = None,
        column: int | str = 0,
    ) -> Any:
        await self._ensure_connection()
        return await self.read_database.fetch_val(query, mapping, column)  # type: ignore

    async def fetch_one(
        self,
        query: str,
        mapping: dict | None = None,
    ) -> Record | None:
        await self._ensure_connection()
        return await self.read_database.fetch_one(query, mapping)  # type: ignore

    async def fetch_all(
        self,
        query: str,
        mapping: dict | None = None,
    ) -> list[Record]:
        await self._ensure_connection()
        return await self.read_database.fetch_all(query, mapping)  # type: ignore

    async def execute(
        self,
        query: str,
        mapping: dict | None = None,
    ) -> Any:  # TODO: typehint
        await self._ensure_connection()
        return await self.write_database.execute(query, mapping)  # type: ignore

    async def execute_many(
        self,
        query: str,
        mapping: dict | None = None,
    ) -> Any:  # TODO: typehint
        await self._ensure_connection()
        return await self.write_database.execute_many(query, mapping)  # type: ignore
