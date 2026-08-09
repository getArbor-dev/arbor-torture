"""Layer 2 module 12. Generated, seed=20260810."""

from deep.l0.m15 import value_m15
from deep.l0.m16 import value_m16
from deep.l0.m20 import value_m20
from deep.l1.m00 import value_m00
from deep.l1.m04 import value_m04
from deep.l1.m06 import value_m06
from deep.l1.m13 import value_m13
from deep.l1.m25 import value_m25

BASE_12 = 212


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m15(n) + value_m16(n) + value_m20(n) + value_m00(n) + value_m04(n) + value_m06(n) + value_m13(n) + value_m25(n)
