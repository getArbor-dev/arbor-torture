"""HTTP entrypoint. GROUND TRUTH: downstream=0 (nothing imports routes)."""

from app.services.auth import current_user, create_session
from app.services.billing import charge, price_for
from app.services.email import send_receipt


def handle_login(token: str):
    user = current_user(token)
    if user is None:
        return {"status": 401}
    return {"status": 200, "session": create_session(user["id"])}


def handle_checkout(token: str, plan: str):
    try:
        result = charge(token, plan)
    except PermissionError:
        return {"status": 401}
    except ValueError:
        return {"status": 400, "error": "unknown plan"}
    send_receipt("user@example.com", result["amount"])
    return {"status": 200, "charged": result["amount"]}


def handle_pricing():
    return {"pro": price_for("pro"), "team": price_for("team")}
