from app.models import BaseModel


class HTMLBody(BaseModel):
    html: str
    raw: str | None
