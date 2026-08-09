"""Layer 4 module 06. Generated, seed=20260810."""

from deep.l2.m19 import value_m19

BASE_06 = 406


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m19(n)
