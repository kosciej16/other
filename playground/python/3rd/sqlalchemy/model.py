from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()
# url = "postgresql://postgres:postgres@127.0.0.1:5432"
# url = "postgresql://postgres:warden@postgres:5432/warden"
url = "postgresql://postgres@127.0.0.1:25432"

engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True)
    num = Column(Integer)


Base.metadata.create_all(engine)
