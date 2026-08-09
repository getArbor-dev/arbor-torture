"""Layer 6 module 08. Generated, seed=20260810."""

from deep.l5.m22 import value_m22

BASE_08 = 608


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m22(n)
