"""Logging hub. GROUND TRUTH: 5 files downstream."""

LEVELS = ("debug", "info", "warn", "error")


def log(level: str, message: str) -> None:
    if level not in LEVELS:
        raise ValueError("unknown level: %s" % level)
    print("[%s] %s" % (level.upper(), message))


def audit(actor: str, action: str) -> None:
    log("info", "audit actor=%s action=%s" % (actor, action))
