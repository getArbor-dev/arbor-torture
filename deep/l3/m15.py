"""Layer 3 module 15. Generated, seed=20260810."""

from deep.l2.m17 import value_m17

BASE_15 = 315


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m17(n)
