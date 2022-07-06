from fastapi import APIRouter, Depends, HTTPException

from api.deps import get_current_user
from models.user import User

router = APIRouter()


@router.get("/")
async def get_user(user: User = Depends(get_current_user)):
    if user:
        return user.json()

    raise HTTPException(status_code=403, detail="Not authorized.")
