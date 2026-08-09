"""Billing. GROUND TRUTH: downstream={routes,admin,nightly}."""

from app.core.db import connect
from app.core.logger import log, audit
from app.services.auth import current_user

PRO_CENTS = 900
TEAM_CENTS = 6000


def price_for(plan: str) -> int:
    if plan == "pro":
        return PRO_CENTS
    if plan == "team":
        return TEAM_CENTS
    raise ValueError("unknown plan: %s" % plan)


def charge(token: str, plan: str) -> dict:
    user = current_user(token)
    if user is None:
        raise PermissionError("not authenticated")
    amount = price_for(plan)
    conn = connect()
    conn.query("INSERT INTO payments VALUES (%d)" % amount)
    audit(user["login"], "charge.%s" % plan)
    return {"amount": amount, "plan": plan}


def refund(payment_id: int) -> bool:
    log("warn", "refunding %d" % payment_id)
    return True
