"""Layer 5 module 02. Generated, seed=20260810."""

from deep.l2.m17 import value_m17
from deep.l4.m00 import value_m00
from deep.l4.m05 import value_m05
from deep.l4.m10 import value_m10
from deep.l4.m18 import value_m18

BASE_02 = 502


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m17(n) + value_m00(n) + value_m05(n) + value_m10(n) + value_m18(n)
