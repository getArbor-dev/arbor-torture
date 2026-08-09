"""Layer 7 module 22. Generated, seed=20260810."""

from deep.l6.m04 import value_m04

BASE_22 = 722


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m04(n)
