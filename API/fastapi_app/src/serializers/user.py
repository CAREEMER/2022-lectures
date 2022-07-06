from typing import Optional

from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


class UserLogin(BaseModel):
    email: str
    password: str


class UserPatch(BaseModel):
    first_name: str
    last_name: str
