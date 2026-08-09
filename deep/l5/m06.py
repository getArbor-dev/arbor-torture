"""Layer 5 module 06. Generated, seed=20260810."""

from deep.l2.m14 import value_m14

BASE_06 = 506


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m14(n)
