from datetime import datetime

from app.models import BaseModel
from app.models.scope import Scope
from app.models.status import Status


class OAuthToken(BaseModel):
    id: int
    user_id: int
    client_id: int
    token: str
    refresh_token: str | None
    scopes: list[Scope]
    status: Status
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    deleted_at: datetime | None

    @property
    def expires_in(self) -> int:
        return int((self.expires_at - datetime.now()).total_seconds())
