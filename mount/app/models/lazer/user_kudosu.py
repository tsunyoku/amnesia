from app.models import BaseModel


class UserKudosu(BaseModel):
    total: int
    available: int
