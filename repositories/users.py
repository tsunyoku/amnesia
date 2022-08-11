from __future__ import annotations

import services
import utils
from models.user import User


async def fetch_by_name(name: str) -> User | None:
    safe_name = utils.make_safe_name(name)

    db_res = await services.database.fetch_one(
        "SELECT * FROM users WHERE safe_name = :safe_name",
        {"safe_name": safe_name},
    )
    if not db_res:
        return None

    return User(**db_res)


async def fetch_by_email(email: str) -> User | None:
    db_res = await services.database.fetch_one(
        "SELECT * FROM users WHERE email = :email",
        {"email": email},
    )
    if not db_res:
        return None

    return User(**db_res)


async def create(
    name: str,
    email: str,
    password_bcrypt: str,
    country: str,
) -> int:
    safe_name = utils.make_safe_name(name)

    user_id = await services.database.fetch_val(
        "INSERT INTO users (name, safe_name, email, password_bcrypt, country) VALUES "
        "(:name, :safe_name, :email, :password_bcrypt, :country) RETURNING id",
        {
            "name": name,
            "safe_name": safe_name,
            "email": email,
            "password_bcrypt": password_bcrypt,
            "country": country,
        },
    )

    return user_id
