from db import Base
from sqlalchemy import Column, Integer, UniqueConstraint


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True)
    num = Column(Integer)
    num2 = Column(Integer)
    __table_args__ = (UniqueConstraint("num", "num2", name="model_num_key"),)
