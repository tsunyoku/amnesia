from app.common.context import Context
from app.models.request_exception import RequestException
from app.models.scope import Scope
from app.models.token import OAuthToken
from app.usecases import tokens as tokens_usecases
from fastapi import Request
from fastapi import status

# TODO: is this name misleading? it authenticates while also checking their scope if it does exist
class ScopeEnforcer:
    def __init__(self, *allowed_scopes: Scope) -> None:
        self.scopes = list(allowed_scopes) + [Scope.ALL]

    async def __call__(self, request: Request) -> OAuthToken:
        token = request.headers.get("Authorization")
        if not token:
            raise RequestException(
                response={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        token_type, token_value = token.split(" ", maxsplit=1)
        if token_type != "Bearer":
            raise RequestException(
                response={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        ctx = Context(request)
        oauth_token = await tokens_usecases.fetch_one(ctx, access_token=token_value)
        if oauth_token is None:
            raise RequestException(
                response={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if not any([scope in self.scopes for scope in oauth_token.scopes]):
            raise RequestException(
                response={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return oauth_token
