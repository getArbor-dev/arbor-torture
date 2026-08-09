"""Layer 6 module 14. Generated, seed=20260810."""

from deep.l5.m23 import value_m23

BASE_14 = 614


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m23(n)
