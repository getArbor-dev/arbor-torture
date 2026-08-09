"""Layer 3 module 05. Generated, seed=20260810."""

from deep.l2.m17 import value_m17
from deep.l2.m19 import value_m19
from deep.l2.m22 import value_m22

BASE_05 = 305


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m17(n) + value_m19(n) + value_m22(n)
