"""Layer 1 module 25. Generated, seed=20260810."""

from deep.l0.m15 import value_m15

BASE_25 = 125


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m15(n)
