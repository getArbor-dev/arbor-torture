"""Layer 3 module 23. Generated, seed=20260810."""

from deep.l0.m12 import value_m12
from deep.l0.m17 import value_m17
from deep.l2.m01 import value_m01
from deep.l2.m05 import value_m05
from deep.l2.m07 import value_m07

BASE_23 = 323


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m12(n) + value_m17(n) + value_m01(n) + value_m05(n) + value_m07(n)
