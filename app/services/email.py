"""Email. GROUND TRUTH: upstream={config,logger}, downstream={routes,nightly}."""

from app.core.config import get_setting, is_feature_enabled
from app.core.logger import log


def send(to: str, subject: str, body: str) -> bool:
    timeout = get_setting("timeout", 30)
    if is_feature_enabled("async_email"):
        log("info", "queued mail to %s (timeout=%s)" % (to, timeout))
        return True
    log("info", "sent mail to %s" % to)
    return True


def send_receipt(to: str, amount_cents: int) -> bool:
    return send(to, "Your receipt", "You paid %d cents" % amount_cents)
