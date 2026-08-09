"""Layer 1 module 22. Generated, seed=20260810."""

from deep.l0.m04 import value_m04
from deep.l0.m15 import value_m15
from deep.l0.m18 import value_m18

BASE_22 = 122


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m04(n) + value_m15(n) + value_m18(n)
