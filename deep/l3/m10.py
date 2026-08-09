"""Layer 3 module 10. Generated, seed=20260810."""

from deep.l2.m06 import value_m06

BASE_10 = 310


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m06(n)
