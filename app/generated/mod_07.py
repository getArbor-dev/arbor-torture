"""Generated module 7. Wide fan-in test on config."""

from app.core.config import get_setting


def compute_07(value: int) -> int:
    return value * get_setting("retries", 3) + 7
