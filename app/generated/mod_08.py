"""Generated module 8. Wide fan-in test on config."""

from app.core.config import get_setting


def compute_08(value: int) -> int:
    return value * get_setting("retries", 3) + 8
