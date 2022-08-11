from __future__ import annotations

import re
from collections import defaultdict
from typing import Mapping

from fastapi import Form
from fastapi import Request
from fastapi import status
from fastapi.responses import ORJSONResponse
from fastapi.responses import Response

import utils
from api.routes import router

USERNAME_REGEX = re.compile(r"^[\w \[\]-]{3,32}$")
EMAIL_REGEX = re.compile(r"^[^@\s]{1,200}@[^@\s\.]{1,30}(?:\.[^@\.\s]{2,24})+$")


@router.post("/users")
async def register_user(
    request: Request,
    username: str = Form(..., alias="user[username]"),
    email: str = Form(..., alias="user[user_email]"),
    password: str = Form(..., alias="user[password]"),
):
    errors: Mapping[str, list[str]] = defaultdict(list)

    if not USERNAME_REGEX.match(username):
        errors["username"].append("Usernames must be between 3 and 32 characters")

    if "_" in username and " " in username:
        errors["username"].append("Usernames cannot contain an underscore and space")

    if not errors["username"]:
        ...  # check username doesn't already exist

    if not EMAIL_REGEX.match(email):
        errors["user_email"].append("You must enter a valid email")

    if not errors["user_email"]:
        ...  # check email doesn't already exist

    if not 8 <= len(password) <= 32:
        errors["password"].append("Passwords must be between 8 and 32 characters")

    if errors:
        return ORJSONResponse(
            content={"form_error": {"user": dict(errors)}},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # create user
    ...

    return Response(content=b"ok")
