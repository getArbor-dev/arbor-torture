"""Layer 3 module 02. Generated, seed=20260810."""

from deep.l2.m05 import value_m05

BASE_02 = 302


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m05(n)
