"""Layer 8 module 14. Generated, seed=20260810."""

from deep.l7.m18 import value_m18

BASE_14 = 814


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m18(n)
