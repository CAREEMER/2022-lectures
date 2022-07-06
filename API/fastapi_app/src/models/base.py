import orjson
from sqlalchemy.orm import declarative_base

from db.postgres import get_async_session

BaseClass = declarative_base()


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseModel(BaseClass):
    __abstract__ = True

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

    def json(self):
        attrs = {c.name: getattr(self, c.name) for c in self.__table__.columns if getattr(self, c.name, False)}
        return self.Config.json_dumps(attrs, default=None)

    def parse_raw(self, data: bytes):
        attrs = self.Config.json_loads(data)
        for key, value in dict(attrs).items():
            setattr(self, key, value)
        return self

    async def create_obj(self):
        async_session = get_async_session()
        async with async_session() as session:
            session.add(self)
            await session.commit()
            await session.refresh(self)
        return self
