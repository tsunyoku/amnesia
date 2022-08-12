from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class UserAccountHistory(BaseModel):
    id: int
    type: Literal["note", "restriction", "silence"]
    timestamp: datetime
    length: int
    description: str | None
