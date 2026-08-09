"""Layer 1 module 02. Generated, seed=20260810."""

from deep.l0.m09 import value_m09

BASE_02 = 102


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m09(n)
