from app.models import BaseModel


class UserProfileBanner(BaseModel):
    id: int
    tournament_id: int
    image: str
