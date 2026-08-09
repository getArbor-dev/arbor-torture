"""Layer 5 module 10. Generated, seed=20260810."""

from deep.l4.m11 import value_m11
from deep.l4.m21 import value_m21

BASE_10 = 510


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m11(n) + value_m21(n)
