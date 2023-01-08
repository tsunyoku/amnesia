from app.common.context import Context
from app.models.group import Group
from app.repositories.groups import GroupsRepository


async def fetch_one(
    ctx: Context,
    id: int | None = None,
    identifier: str | None = None,
    name: str | None = None,
    short_name: str | None = None,
    leader_id: int | None = None,
) -> Group | None:
    repo = GroupsRepository(ctx)
    raw_group = await repo.fetch_one(
        id,
        identifier,
        name,
        short_name,
        leader_id,
    )
    if raw_group is None:
        return None

    return Group.parse_obj(raw_group)


async def fetch_all(
    ctx: Context,
    id: int | None = None,
    identifier: str | None = None,
    name: str | None = None,
    short_name: str | None = None,
    leader_id: int | None = None,
) -> list[Group]:
    repo = GroupsRepository(ctx)
    raw_groups = await repo.fetch_all(
        id,
        identifier,
        name,
        short_name,
        leader_id,
    )

    return [Group.parse_obj(raw_group) for raw_group in raw_groups]


async def create_one(
    ctx: Context,
    identifier: str,
    name: str,
    short_name: str,
    leader_id: int,
    description_markdown: str | None = None,
    playmodes: list[str] | None = None,
    colour: str | None = None,
) -> Group:
    repo = GroupsRepository(ctx)
    raw_group = await repo.create_one(
        identifier,
        name,
        short_name,
        leader_id,
        description_markdown,
        playmodes,
        colour,
    )

    return Group.parse_obj(raw_group)
