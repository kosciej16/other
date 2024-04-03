import pytest
from pytest_postgresql.janitor import DatabaseJanitor
from db import engine, url, Session
import psycopg2


@pytest.fixture
def database():
    # variable definition

    user = "postgres"
    host = "localhost"
    port = 25432
    db_name = "nowa"
    password = "pass"
    with DatabaseJanitor(
        user,
        host,
        port,
        db_name,
        "version",
        password=password,
    ):
        yield psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        # with Session() as s:
        # yield s
