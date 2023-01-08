from datetime import datetime

from app.models import BaseModel


class UserBadge(BaseModel):
    awarded_at: datetime
    description: str
    image_url: str
    url: str
