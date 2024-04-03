from db import Base

from sqlalchemy import JSON, Column, Integer
from sqlalchemy.dialects.postgresql import JSONB, UUID


class WithJson(Base):
    __tablename__ = "with_json"

    id = Column(Integer, primary_key=True)
    num = Column(Integer)

    json = Column(JSON)
