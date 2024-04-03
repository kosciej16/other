from db import Base

from sqlalchemy import Column, Integer, String, Text


class T1(Base):
    __tablename__ = "t1"

    id = Column(Integer, primary_key=True)
    path = Column(Text)
    name = Column(Text)
    field = Column(Text)


class T2(Base):
    __tablename__ = "t2"

    id = Column(Integer, primary_key=True)
    t1_id = Column(Integer)
    t1_field = Column(String)
