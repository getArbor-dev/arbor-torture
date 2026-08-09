"""Layer 8 module 15. Generated, seed=20260810."""

from deep.l7.m02 import value_m02

BASE_15 = 815


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m02(n)
