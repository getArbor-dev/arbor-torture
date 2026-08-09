"""Layer 7 module 18. Generated, seed=20260810."""

from deep.l5.m15 import value_m15
from deep.l6.m02 import value_m02
from deep.l6.m04 import value_m04
from deep.l6.m11 import value_m11
from deep.l6.m18 import value_m18
from deep.l6.m20 import value_m20
from deep.l6.m22 import value_m22
from deep.l6.m24 import value_m24

BASE_18 = 718


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m15(n) + value_m02(n) + value_m04(n) + value_m11(n) + value_m18(n) + value_m20(n) + value_m22(n) + value_m24(n)
