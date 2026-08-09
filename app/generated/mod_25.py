"""Generated module 25. Wide fan-in test on config."""

from app.core.config import get_setting


def compute_25(value: int) -> int:
    return value * get_setting("retries", 3) + 25
