from __future__ import annotations

from pydantic import BaseModel


class ProfileBanner(BaseModel):
    id: int
    tournament_id: int
    image: str
