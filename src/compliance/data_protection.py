from sqlalchemy.orm import Session
from src.models.user import User

class DataProtection:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def anonymize_user_data(self, user_id):
        user = self.db_session.query(User).get(user_id)
        if user:
            user.username = 'anonymized'
            self.db_session.commit()

    def handle_data_request(self, user_id, request_type):
        user = self.db_session.query(User).get(user_id)
        if user and request_type == 'delete':
            self.db_session.delete(user)
            self.db_session.commit()
        elif user and request_type == 'access':
            return user.to_dict()  # Assuming a to_dict method exists in User model
