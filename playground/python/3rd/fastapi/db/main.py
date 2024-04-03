# from sqlalchemy_utils import database_exists, create_database

from sqlalchemy.sql.ddl import AddConstraint
from db import Base, engine, Session as Ses

from models.simple import Simple

from models.foreign import User, Client

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint, MetaData, Table


# if not database_exists(engine.url):
#     create_database(engine.url)
# else:
#     # Connect the database if exists.
#     engine.connect()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

name = "client_user_id_fkey"
fk = ForeignKeyConstraint((Client.user_id,), (User.id,), name=name)
Table(Client.__table__.name, MetaData(), fk)
session.execute(AddConstraint(fk))
session.commit()
Client.__mapper__.add_property("user", relationship(User, backref="clients"))

u = User()
t = Client(user=u)

session.add(t)
session.commit()
