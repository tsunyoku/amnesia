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
