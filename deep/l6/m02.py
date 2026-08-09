"""Layer 6 module 02. Generated, seed=20260810."""

from deep.l4.m23 import value_m23
from deep.l5.m01 import value_m01
from deep.l5.m02 import value_m02
from deep.l5.m05 import value_m05
from deep.l5.m12 import value_m12

BASE_02 = 602


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m23(n) + value_m01(n) + value_m02(n) + value_m05(n) + value_m12(n)
