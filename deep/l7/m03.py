"""Layer 7 module 03. Generated, seed=20260810."""

from deep.l4.m06 import value_m06
from deep.l4.m18 import value_m18
from deep.l5.m15 import value_m15
from deep.l6.m07 import value_m07
from deep.l6.m11 import value_m11
from deep.l6.m12 import value_m12
from deep.l6.m14 import value_m14
from deep.l6.m24 import value_m24

BASE_03 = 703


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m06(n) + value_m18(n) + value_m15(n) + value_m07(n) + value_m11(n) + value_m12(n) + value_m14(n) + value_m24(n)
