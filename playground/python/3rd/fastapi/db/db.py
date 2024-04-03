from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()
# url = "postgresql://postgres:postgres@127.0.0.1:5432"
# url = "postgresql://postgres:warden@postgres:5432/warden"
url = "postgresql://postgres:p@127.0.0.1:25432"
# engine = create_engine(url, echo=True)
engine = create_engine(url, echo=False)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
