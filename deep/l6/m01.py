"""Layer 6 module 01. Generated, seed=20260810."""

from deep.l5.m07 import value_m07

BASE_01 = 601


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m07(n)
