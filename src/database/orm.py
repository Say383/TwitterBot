from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import contextlib
import datetime
import logging

engine = create_engine('sqlite:///twitter_bot.db')  # Replace with your database
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))

@contextlib.contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# Example of using the session_scope
def add_user(username):
    with session_scope() as session:
        new_user = User(username=username)
        session.add(new_user)

# More database operations follow the same pattern...
