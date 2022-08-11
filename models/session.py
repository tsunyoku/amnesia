from __future__ import annotations

from datetime import datetime
from datetime import timedelta
from typing import Literal

from pydantic import BaseModel


class Session(BaseModel):
    id: int
    token_type: Literal["Bearer"]
    access_token: str
    token_expiry: datetime
    refresh_token: str

    @property
    def expires_in(self) -> timedelta:
        return self.token_expiry - datetime.utcnow()
