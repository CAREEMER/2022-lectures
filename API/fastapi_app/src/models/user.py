from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True, nullable=False)
    first_name: str = Column(Text)
    last_name: str = Column(Text)
    email: str = Column(Text, unique=True)
    password: str = Column(Text)


class SessionToken(BaseModel):
    __tablename__ = "tokens"

    id: UUID = Column(UUID, primary_key=True, index=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    user: User = relationship("User", backref="tokens")
