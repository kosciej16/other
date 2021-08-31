from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

import factory

engine = create_engine("postgresql://postgres:a@127.0.0.1", echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)
    # id = Column(Integer, primary_key=True)

    tickets = relationship("Ticket")


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

s = Session()


class TicketFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Ticket
        sqlalchemy_session = s
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    user_id = None


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = s
        sqlalchemy_session_persistence = "commit"

    id = factory.Faker("uuid4")
    # id = factory.Sequence(lambda n: n)
    tickets = factory.RelatedFactory(TicketFactory, user_id=id)


UserFactory()
