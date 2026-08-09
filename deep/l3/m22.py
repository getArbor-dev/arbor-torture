"""Layer 3 module 22. Generated, seed=20260810."""

from deep.l2.m17 import value_m17

BASE_22 = 322


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m17(n)
