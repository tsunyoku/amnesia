import asyncio
import hashlib
import secrets

import bcrypt
from app.common.context import Context


def generate_secret(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


async def verify_bcrypt_password(
    ctx: Context,
    password_md5: str,
    bcrypt_hash: str,
) -> bool:
    cached_md5 = await ctx.bcrypt_cache.get(bcrypt_hash)
    if cached_md5 is not None:
        return password_md5 == cached_md5

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(
        None,
        bcrypt.checkpw,
        password_md5.encode(),
        bcrypt_hash.encode(),
    )
    if result:
        await ctx.bcrypt_cache.set(bcrypt_hash, password_md5)

    return result
