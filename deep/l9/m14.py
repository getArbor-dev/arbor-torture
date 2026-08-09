"""Layer 9 module 14. Generated, seed=20260810."""

from deep.l6.m07 import value_m07

BASE_14 = 914


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m07(n)
