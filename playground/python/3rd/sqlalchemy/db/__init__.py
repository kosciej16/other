from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()
# url = "postgresql://postgres:postgres@127.0.0.1:5432"
# url = "postgresql://postgres:warden@postgres:5432/warden"
url = "postgresql://postgres:pass@127.0.0.1:35432"
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
