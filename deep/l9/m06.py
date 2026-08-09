"""Layer 9 module 06. Generated, seed=20260810."""

from deep.l6.m15 import value_m15
from deep.l6.m24 import value_m24
from deep.l7.m02 import value_m02
from deep.l7.m04 import value_m04
from deep.l8.m10 import value_m10
from deep.l8.m13 import value_m13
from deep.l8.m16 import value_m16
from deep.l8.m25 import value_m25

BASE_06 = 906


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m15(n) + value_m24(n) + value_m02(n) + value_m04(n) + value_m10(n) + value_m13(n) + value_m16(n) + value_m25(n)
