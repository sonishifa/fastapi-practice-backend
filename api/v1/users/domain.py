from .repository import UserRepository

class UserDomain:
    def __init__(self):
        self.__repository = UserRepository()

    def create_user(self, user_data, hashed_password, db):
        return self.__repository.create_user(user_data, hashed_password, db)

    def get_user_by_username(self, username, db):
        return self.__repository.get_user_by_username(username, db)

    def get_user_by_email(self, email, db):
        return self.__repository.get_user_by_email(email, db)

