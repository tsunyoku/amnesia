from app.common.context import Context
from app.models import BaseModel
from app.models.scope import Scope
from app.usecases import clients as clients_usecases
from app.usecases import cryptography as cryptography_usecases
from app.usecases import tokens as tokens_usecases
from app.usecases import users as users_usecases
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Form
from fastapi import status
from fastapi.responses import ORJSONResponse

router = APIRouter()


class OAuthSuccess(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
    refresh_token: str | None  # only given to lazer


class OAuthFail(BaseModel):
    authentication: str | None
    hint: str | None


OAuthResponse = OAuthSuccess | OAuthFail


@router.post("/oauth/token", response_model=OAuthResponse)
async def oauth_token(
    username: str | None = Form(None),
    password: str | None = Form(None),
    grant_type: str = Form(...),
    client_id: int = Form(...),
    client_secret: str = Form(...),
    scope: str = Form(...),
    ctx: Context = Depends(),
) -> ORJSONResponse:
    scopes = [Scope(scope) for scope in scope.split(",")]

    # if they are asking for password grant and are requesting * scope, then they're supposed to be lazer
    if Scope.ALL in scopes:
        if grant_type != "password":
            return ORJSONResponse(
                content={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if username is None or password is None:
            return ORJSONResponse(
                content={"hint": "The username or password is incorrect."},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        if client_id != 5 or client_secret not in (
            "FGc9GAtyHzeQDshWP5Ah7dega8hJACAJpQtw6OXk",  # production
            "3LP2mhUrV89xxzD1YKNndXHEhWWCRLPNKioZ9ymT",  # development
        ):
            return ORJSONResponse(
                content={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        user = await users_usecases.fetch_one(ctx, username=username)
        if user is None:
            return ORJSONResponse(
                content={"hint": "The username or password is incorrect."},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        if not await cryptography_usecases.verify_bcrypt_password(
            ctx,
            cryptography_usecases.hash_md5(password),
            user.bcrypt_password,
        ):
            return ORJSONResponse(
                content={"hint": "The username or password is incorrect."},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
    elif grant_type == "client_credentials":
        # client credentials can only request public or identify scopes
        if any([scope not in (Scope.PUBLIC, Scope.IDENTIFY) for scope in scopes]):
            return ORJSONResponse(
                content={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        oauth_client = await clients_usecases.fetch_one(
            ctx,
            id=client_id,
            secret=client_secret,
        )
        if oauth_client is None:
            return ORJSONResponse(
                content={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        user = await users_usecases.fetch_one(ctx, id=oauth_client.user_id)
        if user is None:
            return ORJSONResponse(
                content={"authentication": "basic"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
    else:
        # TODO: authorisation flow (forum.write, friends.read, chat.write)
        # TODO: delegate in client credentials (for chat bots)
        return ORJSONResponse(
            content={"authentication": "basic"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    oauth_token = await tokens_usecases.create_one(
        ctx,
        user.id,
        client_id,
        scopes,
    )

    return ORJSONResponse(
        content=OAuthSuccess(
            token_type="Bearer",
            expires_in=oauth_token.expires_in,
            access_token=oauth_token.token,
            refresh_token=oauth_token.refresh_token,
        ),
        status_code=status.HTTP_200_OK,
    )
