"""Layer 5 module 23. Generated, seed=20260810."""

from deep.l4.m02 import value_m02

BASE_23 = 523


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m02(n)
