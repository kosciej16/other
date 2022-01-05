from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declared_attr


class Base(object):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(320))
    name = Column(String(320))
