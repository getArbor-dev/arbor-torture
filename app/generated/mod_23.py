"""Generated module 23. Wide fan-in test on config."""

from app.core.config import get_setting


def compute_23(value: int) -> int:
    return value * get_setting("retries", 3) + 23
