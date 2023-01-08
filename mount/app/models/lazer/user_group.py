from app.models.lazer.group import Group


class UserGroup(Group):
    playmodes: list[str] | None
