
class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user_info(self, user_id):
        return self.user_service.fetch_user(user_id)
