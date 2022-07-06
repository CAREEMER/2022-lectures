from fastapi import APIRouter, Depends, HTTPException

from serializers.user import UserLogin, UserRegister
from services.auth import AuthService, get_auth_service

router = APIRouter()


@router.post("/register")
async def register_user(user_data: UserRegister, auth_service: AuthService = Depends(get_auth_service)):
    response = await auth_service.register_user(user_data)

    return response.json()


@router.post("/login")
async def login_user(user_data: UserLogin, auth_service: AuthService = Depends(get_auth_service)):
    auth_token = await auth_service.login(user_data)

    if auth_token:
        return auth_token.id

    raise HTTPException(status_code=404, detail="Wrong email or password.")
