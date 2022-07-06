from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import app_config

engine = create_async_engine(app_config.DATABASE_URL, echo=False, future=True)


def get_async_session():
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def yield_session() -> AsyncSession:
    async_session = get_async_session()
    async with async_session() as session:
        yield session
