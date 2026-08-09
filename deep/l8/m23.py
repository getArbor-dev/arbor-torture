"""Layer 8 module 23. Generated, seed=20260810."""

from deep.l6.m09 import value_m09
from deep.l7.m15 import value_m15
from deep.l7.m17 import value_m17
from deep.l7.m20 import value_m20
from deep.l7.m25 import value_m25

BASE_23 = 823


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m09(n) + value_m15(n) + value_m17(n) + value_m20(n) + value_m25(n)
