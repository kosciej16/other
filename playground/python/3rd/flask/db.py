from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models import Base

engine = create_engine("postgresql://127.0.0.1:25432")
Session = sessionmaker(bind=engine)

Base = declarative_base(cls=Base)


def init_app(app):
    Base.metadata.bind = engine
    Session.configure(bind=engine)
    app.session = scoped_session(Session)


db_session = Session()
