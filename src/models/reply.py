
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Reply(Base):
    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)
    content = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    tweet_id = Column(Integer, ForeignKey('tweets.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    # Relationships to the Tweet and User models
    tweet = relationship('Tweet', backref='replies')
    author = relationship('User', backref='replies')

    # Additional attributes and methods for the Reply model can be added here
