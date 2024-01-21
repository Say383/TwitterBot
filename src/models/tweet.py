
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .base import Base
from datetime import datetime

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    content = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))

    # Additional attributes and methods for the Tweet model can be added here
