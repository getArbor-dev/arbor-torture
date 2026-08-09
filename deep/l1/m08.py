"""Layer 1 module 08. Generated, seed=20260810."""

from deep.l0.m09 import value_m09

BASE_08 = 108


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m09(n)
