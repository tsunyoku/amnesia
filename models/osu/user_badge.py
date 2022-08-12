from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class UserBadge(BaseModel):
    url: str
    image_url: str
    description: str
    awarded_at: datetime
