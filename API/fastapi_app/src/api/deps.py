import aioredis
from fastapi import Depends
from fastapi.security import APIKeyHeader
from starlette.exceptions import HTTPException
from starlette.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST

from core.config import app_config
from models.user import User
from services.auth import AuthService, get_auth_service

REDIS_IDEMPOTENCY_KEY_EXPIRES_IN = 30


oauth2_scheme = APIKeyHeader(name="Authorization")
idempotency_key_scheme = APIKeyHeader(
    name="Idempotency-Key", description="Idempotency key.", scheme_name="Idempotency Key", auto_error=False
)


async def get_current_user(
    token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)
) -> User:
    user = await auth_service.login_with_token(token)
    return user


async def pagination_parameters(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}


async def idempotent_request(idempotency_key: str = Depends(idempotency_key_scheme)):
    if not idempotency_key:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Provide 'Idempotency-Key' header.")

    redis = aioredis.from_url(app_config.REDIS_DSN)

    redis_key = app_config.IDEMPOTENCY_KEY_PREFIX + f"**{idempotency_key}"
    exist = await redis.get(redis_key)

    if exist:
        raise HTTPException(status_code=HTTP_202_ACCEPTED, detail="Already accepted.")

    await redis.set(redis_key, "1", ex=REDIS_IDEMPOTENCY_KEY_EXPIRES_IN)
