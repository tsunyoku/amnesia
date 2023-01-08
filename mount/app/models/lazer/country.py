from app.models import BaseModel


class Country(BaseModel):
    code: str
    name: str
