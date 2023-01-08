from datetime import datetime

from app.models import BaseModel


class UserRankHighest(BaseModel):
    rank: int
    updated_at: datetime
