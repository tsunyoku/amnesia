from datetime import datetime

from app.models import BaseModel


class UserAchievement(BaseModel):
    achieved_at: datetime
    achievement_id: int
