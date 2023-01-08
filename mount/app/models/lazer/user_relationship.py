from enum import Enum

from app.models import BaseModel
from app.models.lazer.user_compact import UserCompact


class UserRelationshipType(str, Enum):
    FRIEND = "friend"
    BLOCK = "block"


class UserRelationship(BaseModel):
    target_id: int
    relation_type: object
    mutual: bool
    target: UserCompact | None
