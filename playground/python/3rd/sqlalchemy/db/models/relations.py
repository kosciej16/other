from db import Base
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)

    tickets = relationship("Ticket")


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)


class Child(Base):
    __tablename__ = "child"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer)
    other_id = Column(Integer)

    parent = relationship(
        "Parent",
        foreign_keys=[parent_id, other_id],
        # primaryjoin="Child.parent_id == Parent.id and Child.other_id == Parent.other_id",
        primaryjoin="and_(Child.parent_id == Parent.id, Child.other_id == Parent.other_id)",
        back_populates="child",
        uselist=False,
    )


class Parent(Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True)
    other_id = Column(Integer)
    # child = relationship("Child", uselist=False)
    p1 = Column(Integer)
    p2 = Column(Integer)
    p3 = Column(Integer)
    child = relationship(
        "Child",
        foreign_keys=[Child.parent_id, Child.other_id],
        primaryjoin="Parent.id == Child.parent_id and Child.other_id == Parent.other_id",
        # primaryjoin="Parent.id == foreign(Child.parent_id)",
        uselist=False,
    )
