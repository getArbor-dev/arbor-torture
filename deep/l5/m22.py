"""Layer 5 module 22. Generated, seed=20260810."""

from deep.l3.m22 import value_m22

BASE_22 = 522


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m22(n)
