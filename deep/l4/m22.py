"""Layer 4 module 22. Generated, seed=20260810."""

from deep.l1.m05 import value_m05
from deep.l1.m20 import value_m20
from deep.l2.m12 import value_m12
from deep.l3.m01 import value_m01
from deep.l3.m09 import value_m09
from deep.l3.m22 import value_m22
from deep.l3.m23 import value_m23
from deep.l3.m25 import value_m25

BASE_22 = 422


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m05(n) + value_m20(n) + value_m12(n) + value_m01(n) + value_m09(n) + value_m22(n) + value_m23(n) + value_m25(n)
