import random
import string
from typing import Iterable

from sqlalchemy import TEXT, Column, MetaData, Table, and_, text
from sqlalchemy.orm import aliased
from db import Base, Session, engine
from db.models.join import T1, T2


import logging

from utils import pretty_format_sql, query_to_sql

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)


def rand(k=5):
    return "".join(random.choices(string.ascii_lowercase, k=k))


def reset():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    paths = []
    cols = [Column("parent_path", TEXT), Column("name", TEXT)]
    with Session() as s:
        # s.execute(text("DROP TABLE tmp"))
        # s.execute(text("CREATE TABLE tmp (path text, name text)"))
        s.add(T1(path="/", name="b"))
        s.add(T1(path="/", name="c"))
        s.add(T1(path="/", name="e"))
        s.add(T1(path="/", name="d"))
        s.add(T1(path="/dir", name="a"))
        s.add(T1(path="/dir", name="f"))
        s.add(T1(path="/dir2", name="g"))
        s.add(T1(path="/", name="b"))

        # p = "/home/kosciej/very_long_path_very_very"
        # for id_ in range(10):
        #     for name in ("env", "script", rand()):
        #         fp = f"{p}/{id_}"
        #         if id_ % 2:
        #             paths.append((fp, "env"))
        #         if id_ % 3:
        #             paths.append((fp, "script"))
        #         if not id_ % 5 and name not in ("env", "script"):
        #             paths.append((fp, name))
        #         t1 = T1(path=fp, name=name, field=rand())
        #         s.add(t1)
        paths = [("/", "d"), ("/dir", "a"), ("/dir", "f"), ("/", "a"), ("/", "d"), ("/", "d"), ("/", "d"), ("/", "d")]
        # dir/a
        # dir/f
        # a
        # d
        # d
        # d
        # d

        table = create_temp_table_from_tuples(s, "tabelka", cols, paths, debug_sql=False)
        table2 = aliased(table)
        q = s.query(T1).join(table, T1.path == table.c.parent_path)
        q = q.join(table2, T1.name == table2.c.name)
        # s.execute(text("SET enable_hashjoin = off"))
        # subq = s.query(table).distinct().subquery("dupa")
        # al = aliased(T2, subq)
        # q = q.join(al, T1.name == subq.c.name)
        # for r in q:
        # sql = query_to_sql(s, q)
        # print(sql)
        # explain_sql = f"EXPLAIN ANALYZE {sql}"
        # result = s.execute(text(sql))
        for row in q:
            print(row.path, row.name)

        # print(q.statement)
        # print(query_to_sql(s, q))
        # for p in paths:
        # s.execute(text(f"insert into tmp values {','.join(paths)}"))
        # s.execute(text(f"insert into tmp values {p}"))
        # s.commit()


def logged_execute(session, stmt, debug_sql):
    if debug_sql:
        sql = query_to_sql(session, stmt)
        logger.debug("Query: \n%s", pretty_format_sql(sql))
    return session.execute(stmt)


def create_temp_table_from_tuples(
    session,
    table_name,
    columns,
    tuple_gen,
    debug_sql=False,
    # debug_temp_tables=False,
    # stat_prefix="",
    # alias=None,
    # with_index=None,
):
    ret = Table(table_name, MetaData(), *columns)

    columns_stmt = ", ".join(f"{col.name} {col.type}" for col in columns)
    create_table_stmt = text(f"CREATE TEMP TABLE {table_name} ({columns_stmt}) ON COMMIT DROP")
    logged_execute(session, create_table_stmt, debug_sql=debug_sql)

    if isinstance(tuple_gen, str):
        session.execute(f"INSERT INTO {table_name} ({tuple_gen})")
    elif isinstance(tuple_gen, Iterable):
        for tup in tuple_gen:
            session.execute(text(f"INSERT INTO {table_name} values {tup}"))
    #     raw_conn = session.connection().connection
    #     pg_copier = PgCopier(table_name, raw_conn)
    #     if debug_sql:
    #         logger.debug("Copying paths to %s", table_name)
    #     pg_copier.copy_from_tuples(
    #         tuple_gen, [col.name for col in columns], measure_time_prefix=stat_prefix
    #     )
    # else:
    #     raise TypeError(f"Unsupported tuple source: {tuple_gen}")

    logged_execute(session, text(f"ANALYZE {table_name}"), debug_sql=debug_sql)
    # if with_index:
    #     _create_index_on_temp_table(session, table_name, with_index, debug_sql)
    return ret


reset()
