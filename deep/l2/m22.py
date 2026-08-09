"""Layer 2 module 22. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m12 import value_m12
from deep.l1.m01 import value_m01
from deep.l1.m20 import value_m20
from deep.l1.m25 import value_m25

BASE_22 = 222


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m00(n) + value_m12(n) + value_m01(n) + value_m20(n) + value_m25(n)
