from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(tags=["osu!lazer API"], default_response_class=ORJSONResponse)
