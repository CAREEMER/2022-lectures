from typing import Optional

from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    text: Optional[str]
