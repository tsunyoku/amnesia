from datetime import datetime
from enum import Enum

from app.models import BaseModel


class UserAccountHistoryType(str, Enum):
    NOTE = "note"
    RESTRICTION = "restriction"
    SILENCE = "silence"
    TOURNAMENT_BAN = "tournament_ban"


class UserAccountHistory(BaseModel):
    id: int
    timestamp: datetime
    legnth: int
    permanent: bool
    type: UserAccountHistoryType
    description: str | None
