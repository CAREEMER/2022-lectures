from typing import Dict

from models.user import User


class Database:
    USER_DATABASE: Dict[str, User] = {}

    async def connect(self):
        """Connects to the database."""
        ...

    @classmethod
    async def get_user_with_email_and_password(cls, email: str, password: str) -> User:
        user = None

        for _user in cls.USER_DATABASE.values():
            if _user.email == email and _user.password == password:
                user = _user

        if not user:
            raise Exception("User not found.")

        return user

    @classmethod
    async def get_user_with_id(cls, _id: str) -> User:
        user = cls.USER_DATABASE.get(_id)

        if not user:
            raise Exception("User not found.")

        return user

    async def disconnect(self):
        """Disconnects from the database."""
        ...


def generate_user_database():
    for _ in range(3):
        user = User()
        Database.USER_DATABASE[str(user.id)] = user
