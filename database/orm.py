
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///twitter_bot.db')  # Replace with your database
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_user(username):
    session = Session()
    new_user = User(username=username)
    session.add(new_user)
    session.commit()

def add_tweet(content, user_id):
    session = Session()
    new_tweet = Tweet(content=content, user_id=user_id)
    session.add(new_tweet)
    session.commit()
