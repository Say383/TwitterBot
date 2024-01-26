from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

# Database Configurations
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///twitter_bot.db')

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    tweets = relationship('Tweet', backref='author')

class Tweet(Base):
    __tablename__ = 'tweets'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship(User, backref='tweets')

# Function to initialize the database (to be run once)
def init_db():
    Base.metadata.create_all(engine)

# Database connection setup (this should be configured with real database URI)
engine = create_engine('sqlite:///twitter_bot.db', echo=True)
Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()
