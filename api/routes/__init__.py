from fastapi.responses import ORJSONResponse
from fastapi import APIRouter

router = APIRouter(tags=["osu!lazer API"], default_response_class=ORJSONResponse)
