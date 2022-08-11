from __future__ import annotations

import asyncio

import bcrypt

CACHE: dict[str, str] = {}


async def verify(plain_password: str, hashed_password: str) -> bool:
    if hashed_password in CACHE:
        return CACHE[hashed_password] == plain_password

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(
        None,
        bcrypt.checkpw,
        plain_password.encode(),
        hashed_password.encode(),
    )

    if result:
        CACHE[hashed_password] = plain_password

    return result
