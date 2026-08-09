"""Layer 5 module 04. Generated, seed=20260810."""

from deep.l4.m00 import value_m00

BASE_04 = 504


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m00(n)
