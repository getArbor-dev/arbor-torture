"""Layer 2 module 18. Generated, seed=20260810."""

from deep.l0.m05 import value_m05
from deep.l0.m10 import value_m10
from deep.l0.m19 import value_m19

BASE_18 = 218


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m05(n) + value_m10(n) + value_m19(n)
