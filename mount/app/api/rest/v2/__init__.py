from fastapi import APIRouter

router = APIRouter()

from .oauth import router as oauth_router
from .users import router as users_router

router.include_router(oauth_router, tags=["oauth"])
router.include_router(users_router, tags=["users"])
