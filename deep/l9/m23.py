"""Layer 9 module 23. Generated, seed=20260810."""

from deep.l7.m12 import value_m12

BASE_23 = 923


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m12(n)
