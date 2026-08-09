"""Layer 5 module 12. Generated, seed=20260810."""

from deep.l4.m03 import value_m03

BASE_12 = 512


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m03(n)
