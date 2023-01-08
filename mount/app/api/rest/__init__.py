from fastapi import APIRouter

from .v2 import router as v2_router

router = APIRouter()
router.include_router(v2_router)
