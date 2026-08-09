"""Layer 4 module 24. Generated, seed=20260810."""

from deep.l1.m19 import value_m19
from deep.l3.m20 import value_m20

BASE_24 = 424


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m19(n) + value_m20(n)
