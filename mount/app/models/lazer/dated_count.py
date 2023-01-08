from datetime import datetime

from app.models import BaseModel
from pydantic import validator


class DatedCount(BaseModel):
    start_date: datetime
    count: int

    @validator("start_date", pre=True)
    def _date_validator(cls, date_str: str) -> datetime:
        return datetime.strptime(date_str, "%Y-%m-%d")
