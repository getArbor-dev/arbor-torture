"""Layer 7 module 15. Generated, seed=20260810."""

from deep.l4.m19 import value_m19
from deep.l6.m13 import value_m13
from deep.l6.m22 import value_m22

BASE_15 = 715


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m19(n) + value_m13(n) + value_m22(n)
