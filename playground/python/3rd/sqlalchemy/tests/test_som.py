from sqlalchemy import text


def test_som(database):
    with database:
        with database.cursor() as curs:
            curs.execute("select * from model")
    pass
