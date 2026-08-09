"""Layer 9 module 18. Generated, seed=20260810."""

from deep.l6.m06 import value_m06
from deep.l7.m23 import value_m23

BASE_18 = 918


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m06(n) + value_m23(n)
