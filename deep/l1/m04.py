"""Layer 1 module 04. Generated, seed=20260810."""

from deep.l0.m24 import value_m24

BASE_04 = 104


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m24(n)
