from fastapi import Depends
from fastapi.security import APIKeyHeader

from models.user import User
from services.auth import AuthService, get_auth_service

oauth2_scheme = APIKeyHeader(name="Authorization")


async def get_current_user(
    token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)
) -> User:
    user = await auth_service.login_with_token(token)
    return user
