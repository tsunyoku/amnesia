from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from . import oauth
from . import register

router = APIRouter(tags=["osu!lazer API"], default_response_class=ORJSONResponse)
