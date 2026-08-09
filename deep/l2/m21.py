"""Layer 2 module 21. Generated, seed=20260810."""

from deep.l0.m17 import value_m17

BASE_21 = 221


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m17(n)
