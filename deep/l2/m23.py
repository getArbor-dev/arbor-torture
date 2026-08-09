"""Layer 2 module 23. Generated, seed=20260810."""

from deep.l0.m19 import value_m19
from deep.l1.m15 import value_m15

BASE_23 = 223


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m19(n) + value_m15(n)
