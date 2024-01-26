from sqlalchemy import LargeBinary
from werkzeug.security import generate_password_hash

# src/models/user.py
class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(LargeBinary)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    date_joined = Column(DateTime, default=datetime.utcnow)
    profile_picture_url = Column(String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
