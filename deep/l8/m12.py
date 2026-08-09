"""Layer 8 module 12. Generated, seed=20260810."""

from deep.l5.m06 import value_m06
from deep.l5.m24 import value_m24
from deep.l6.m20 import value_m20
from deep.l7.m08 import value_m08
from deep.l7.m10 import value_m10
from deep.l7.m12 import value_m12
from deep.l7.m13 import value_m13
from deep.l7.m14 import value_m14

BASE_12 = 812


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m06(n) + value_m24(n) + value_m20(n) + value_m08(n) + value_m10(n) + value_m12(n) + value_m13(n) + value_m14(n)
