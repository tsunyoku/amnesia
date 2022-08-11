from __future__ import annotations

from pydantic import BaseModel


class Geolocation(BaseModel):
    longitude: float
    latitude: float

    iso_code: str
