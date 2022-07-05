from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
import names

from models.factory import generate_password, generate_email


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(default_factory=names.get_first_name)
    last_name: str = Field(default_factory=names.get_last_name)
    email: EmailStr = Field(default_factory=generate_email)
    password: str = Field(default_factory=generate_password)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
