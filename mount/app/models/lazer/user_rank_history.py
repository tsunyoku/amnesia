from app.models import BaseModel


class UserRankHistory(BaseModel):
    mode: str
    data: list[int]
