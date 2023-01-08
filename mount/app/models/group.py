from app.models import BaseModel


class Group(BaseModel):
    id: int
    identifier: str
    name: str
    short_name: str
    description_markdown: str | None
    playmodes: list[str] | None
    colour: str | None
    leader_id: int
