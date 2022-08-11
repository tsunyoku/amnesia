from api.routes import router
from api import responses


@router.post("/oauth")
async def oauth_token() -> responses.APIResponse:
    ...
