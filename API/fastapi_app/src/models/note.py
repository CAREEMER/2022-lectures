from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.base import BaseModel


class Note(BaseModel):
    __tablename__ = "notes"

    id: int = Column(Integer, primary_key=True, index=True, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now)
    title: str = Column(String, nullable=False)
    text: str = Column(Text, nullable=False)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="notes")
