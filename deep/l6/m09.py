"""Layer 6 module 09. Generated, seed=20260810."""

from deep.l4.m23 import value_m23

BASE_09 = 609


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m23(n)
