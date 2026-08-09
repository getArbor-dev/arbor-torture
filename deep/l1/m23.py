"""Layer 1 module 23. Generated, seed=20260810."""

from deep.l0.m01 import value_m01
from deep.l0.m05 import value_m05
from deep.l0.m09 import value_m09
from deep.l0.m12 import value_m12
from deep.l0.m20 import value_m20

BASE_23 = 123


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m01(n) + value_m05(n) + value_m09(n) + value_m12(n) + value_m20(n)
