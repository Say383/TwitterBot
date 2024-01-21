
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    tweets = relationship('Tweet', back_populates='author')

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    content = Column(String(280))
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    author = relationship('User', back_populates='tweets')

engine = create_engine('sqlite:///twitter_bot.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
