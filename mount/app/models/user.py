from datetime import datetime

from app.models import BaseModel
from app.models.status import Status


class User(BaseModel):
    id: int
    username: str
    email: str
    country_acronym: str
    bcrypt_password: str
    privileges: int
    default_mode: str
    friend_only_dms: bool
    show_status: bool
    last_visit: datetime
    restricted_at: datetime | None
    supporter_until: datetime | None
    userpage_bbcode: str | None
    default_group: int
    status: Status
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
