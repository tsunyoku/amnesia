from datetime import datetime

from app.models import BaseModel
from app.models.status import Status


class OAuthClient(BaseModel):
    id: int
    user_id: int
    name: str
    secret: str
    status: Status
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
