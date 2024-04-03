import sqlparse
import json

from sqlalchemy.dialects.postgresql.json import JSON, JSONB

from sqlalchemy.engine import Row
from db import engine


def explain(query, session):
    st = query.statement.compile(engine, compile_kwargs={"literal_binds": True})
    print(st)
    res = session.execute(f"explain {st}")
    print(res)


def ensure_unicode(unicode_or_binary, try_surrogate_escape=False, replace_invalid=False):
    """
    Ensure that given unicode or binary will be a unicode object.

    >>> ensure_unicode(b'abc') == u'abc'
    True
    >>> ensure_unicode(u'abcd') == u'abcd'
    True
    >>> ensure_unicode(CORRECT_UNICODE) == CORRECT_UNICODE
    True
    >>> ensure_unicode(CORRECT_UTF8_BINARY) == CORRECT_UNICODE
    True
    >>> ensure_unicode(SURROGATES_UNICODE) == SURROGATES_UNICODE
    True
    >>> __is_raised(UnicodeDecodeError, lambda: ensure_unicode(INCORRECT_UTF8_BINARY))
    True
    >>> ensure_unicode(INCORRECT_UTF8_BINARY, try_surrogate_escape=True) == SURROGATES_UNICODE
    True
    """
    if try_surrogate_escape and replace_invalid:
        raise ValueError("try_surrogate_escape and replace_invalid cannot both be True")
    if isinstance(unicode_or_binary, bytes):
        try:
            return unicode_or_binary.decode("utf-8", "replace" if replace_invalid else "strict")
        except UnicodeDecodeError:
            if try_surrogate_escape:
                return unicode_or_binary.decode("utf-8", "surrogateescape")
            else:
                raise
    return unicode_or_binary


def query_to_sql(session, query):
    if isinstance(query, str):
        return query
    stmt = query.statement if hasattr(query, "statement") else query
    compiled_stmt = stmt.compile(session.get_bind())
    # hack for https://github.com/sqlalchemy/sqlalchemy/issues/6114
    expanded_state = compiled_stmt._process_parameters_for_postcompile(compiled_stmt.params)

    raw_conn = session.connection().connection
    with raw_conn.cursor() as cur:
        params = expanded_state.additional_parameters
        for k, v in params.items():
            param_bind = compiled_stmt.binds.get(k)
            if param_bind is not None and isinstance(param_bind.type, (JSON, JSONB)):
                params[k] = json.dumps(v)
            elif isinstance(v, Row):
                # value comes from another query; in SQLAlchemy 1.3  the type was sqlalchemy.util._collections.result
                # this has changed in 1.4: https://docs.sqlalchemy.org/en/14/changelog/migration_14.html
                # #rowproxy-is-no-longer-a-proxy-is-now-called-row-and-behaves-like-an-enhanced-named-tuple
                params[k] = tuple(v)
        query_string = cur.mogrify(expanded_state.statement, params)
        return ensure_unicode(query_string)


def pretty_format_sql(sql):
    # formatting long sql queries takes very long time
    # In case of sql with 10 000 characters it is around 0.3s
    if len(sql) > 10000:
        return sql
    else:
        return sqlparse.format(sql, reindent=True, keyword_case="upper")
