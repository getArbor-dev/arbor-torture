"""Layer 7 module 09. Generated, seed=20260810."""

from deep.l6.m19 import value_m19

BASE_09 = 709


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m19(n)
