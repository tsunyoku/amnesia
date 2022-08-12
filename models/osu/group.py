from __future__ import annotations

from pydantic import BaseModel


class Group(BaseModel):
    id: int
    identifier: str
    name: str
    short_name: str
    colour: str | None
    is_probationary: bool
    has_playmodes: bool
    has_listing: bool
