# from db import Base

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
