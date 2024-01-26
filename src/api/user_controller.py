class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user_info(self, user_id):
        # Fetch user info from UserService
        user = self.user_service.fetch_user(user_id)
        return user.to_dict() if user else None
