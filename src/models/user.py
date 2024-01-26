# src/models/user.py
class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)  # New field added
