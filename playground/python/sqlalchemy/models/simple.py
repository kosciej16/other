from db import Base

from sqlalchemy import Column, Integer


class Simple(Base):
    __tablename__ = "simple"

    id = Column(Integer, primary_key=True)
    num = Column(Integer)
