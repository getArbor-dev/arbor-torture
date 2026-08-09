"""Layer 6 module 21. Generated, seed=20260810."""

from deep.l5.m24 import value_m24

BASE_21 = 621


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m24(n)
