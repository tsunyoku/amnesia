from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    safe_name: str
    email: str
    password_bcrypt: str
    privileges: int  # TOOD: enum?
    country: str
    creation_time: datetime

    def __repr__(self) -> str:
        return f"<{self.name} ({self.id})>"
