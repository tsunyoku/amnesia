from app.models import BaseModel
from app.models.lazer.description import Description


class Group(BaseModel):
    colour: str | None
    has_listing: bool
    has_playmodes: bool
    id: int
    identifier: str
    is_probationary: bool
    name: str
    short_name: str
    description: Description | None
