"""Layer 6 module 12. Generated, seed=20260810."""

from deep.l3.m04 import value_m04
from deep.l4.m00 import value_m00
from deep.l4.m23 import value_m23
from deep.l5.m01 import value_m01
from deep.l5.m07 import value_m07
from deep.l5.m09 import value_m09
from deep.l5.m13 import value_m13
from deep.l5.m15 import value_m15

BASE_12 = 612


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m04(n) + value_m00(n) + value_m23(n) + value_m01(n) + value_m07(n) + value_m09(n) + value_m13(n) + value_m15(n)
