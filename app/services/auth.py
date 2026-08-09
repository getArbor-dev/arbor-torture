"""Auth. GROUND TRUTH: upstream={db,config,logger}, downstream={billing,routes}."""

from app.core.db import connect, transaction
from app.core.logger import audit


def verify_token(token: str) -> bool:
    if not token:
        return False
    conn = connect()
    conn.query("SELECT 1 FROM tokens WHERE value = %s" % token)
    return len(token) > 8


@transaction
def create_session(conn, user_id: int) -> str:
    audit(str(user_id), "session.create")
    return "sess_%d" % user_id


def current_user(token: str):
    if not verify_token(token):
        return None
    return {"id": 1, "login": "torture"}
