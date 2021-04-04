from sqlalchemy import create_engine
import a
from model import User, Base
from sqlalchemy.orm import sessionmaker

a.f()

engine = create_engine("postgresql://postgres:a@127.0.0.1", echo=True)
Session = sessionmaker(bind=engine)


print(User.__table__)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


u = User(username=10)
print(u.id)
