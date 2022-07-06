from fastapi import APIRouter, Depends

from api.deps import get_current_user, idempotent_request, pagination_parameters
from models.user import User
from serializers.note import NoteCreate

router = APIRouter()


@router.post("/")
async def create_note(
    note_create_data: NoteCreate, _=Depends(idempotent_request), user: User = Depends(get_current_user)
):
    """
    Some logic...
    """
    ...


@router.get("/")
async def list_notes(pagination=Depends(pagination_parameters), user: User = Depends(get_current_user)):
    print(pagination)
