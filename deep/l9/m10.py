"""Layer 9 module 10. Generated, seed=20260810."""

from deep.l6.m09 import value_m09
from deep.l8.m07 import value_m07

BASE_10 = 910


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m09(n) + value_m07(n)
