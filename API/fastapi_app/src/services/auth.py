from functools import lru_cache
from uuid import uuid4

from sqlalchemy import select

from db.postgres import get_async_session
from models.user import SessionToken, User
from serializers.user import UserLogin, UserRegister


class AuthService:
    def __init__(self):
        self.async_session = get_async_session()

    async def register_user(self, user_register_data: UserRegister):
        user = User()

        user.email = user_register_data.email
        user.last_name = user_register_data.last_name
        user.first_name = user_register_data.first_name
        user.password = user_register_data.password

        return await user.create_obj()

    async def login(self, user_login_data: UserLogin):
        async with self.async_session() as session:
            user_id = (
                (
                    await session.execute(
                        select(User.id)
                        .where(User.email == user_login_data.email)
                        .where(User.password == user_login_data.password)
                    )
                )
                .scalars()
                .first()
            )

        if user_id:
            token = SessionToken()
            token.id = str(uuid4())
            token.user_id = user_id
            return await token.create_obj()

    async def login_with_token(self, token: str):
        async with self.async_session() as session:
            user_id = (
                (await session.execute(select(SessionToken.user_id).where(SessionToken.id == token))).scalars().first()
            )

        if user_id:
            user = (await session.execute(select(User).where(User.id == user_id))).scalars().first()

            print(type(user))
            return user


@lru_cache()
def get_auth_service() -> AuthService:
    return AuthService()
