"""Configuration hub. GROUND TRUTH: 7 files downstream."""

DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3


def get_setting(name: str, fallback=None):
    """Read a setting. Called from db, email, and transitively everywhere."""
    table = {"timeout": DEFAULT_TIMEOUT, "retries": MAX_RETRIES}
    return table.get(name, fallback)


def get_database_url() -> str:
    return "postgresql://localhost:5432/torture"


def is_feature_enabled(flag: str) -> bool:
    return flag in {"billing_v2", "async_email"}
