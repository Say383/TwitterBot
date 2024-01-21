
from src.models.user import User
from src.utils.logger import Logger
from src.services.auth import AuthService
from flask import request, session

class UserController:
    def __init__(self, auth_service: AuthService, logger: Logger):
        self.auth_service = auth_service
        self.logger = logger

    def login(self, username, password):
        # Authenticate user
        user = self.auth_service.authenticate(username, password)
        if user:
            session['user_id'] = user.id
            return True
        else:
            self.logger.log_error('Login failed')
            return False

    def logout(self):
        # Logout user
        session.pop('user_id', None)

    def register(self, username, password):
        # Register new user
        if self.auth_service.register_new_user(username, password):
            return True
        else:
            self.logger.log_error('Registration failed')
            return False

    def get_current_user(self):
        # Retrieve the currently logged-in user
        user_id = session.get('user_id')
        if user_id:
            return self.auth_service.get_user_by_id(user_id)
        return None
