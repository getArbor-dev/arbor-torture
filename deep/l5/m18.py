"""Layer 5 module 18. Generated, seed=20260810."""

from deep.l2.m18 import value_m18
from deep.l3.m15 import value_m15

BASE_18 = 518


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m18(n) + value_m15(n)
