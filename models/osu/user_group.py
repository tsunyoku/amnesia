from __future__ import annotations

from .group import Group


class UserGroup(Group):
    playmodes: list[str] | None
