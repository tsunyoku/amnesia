from app.models import BaseModel


class UserProfileCover(BaseModel):
    url: str
    custom_url: str | None
    id: str | None
