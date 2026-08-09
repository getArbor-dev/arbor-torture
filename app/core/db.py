"""Database layer. GROUND TRUTH: upstream=config, downstream=5."""

from app.core.config import get_database_url, get_setting
from app.core.logger import log


class Connection:
    def __init__(self, url: str):
        self.url = url
        self.timeout = get_setting("timeout", 30)

    def query(self, sql: str):
        log("debug", "query: %s" % sql[:40])
        return []


def connect() -> Connection:
    return Connection(get_database_url())


def transaction(fn):
    def wrapper(*args, **kwargs):
        conn = connect()
        log("debug", "begin transaction")
        return fn(conn, *args, **kwargs)
    return wrapper
