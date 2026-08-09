"""Layer 3 module 21. Generated, seed=20260810."""

from deep.l2.m04 import value_m04

BASE_21 = 321


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m04(n)
