"""Layer 8 module 25. Generated, seed=20260810."""

from deep.l5.m09 import value_m09
from deep.l5.m22 import value_m22
from deep.l6.m02 import value_m02
from deep.l6.m24 import value_m24
from deep.l7.m03 import value_m03
from deep.l7.m16 import value_m16
from deep.l7.m17 import value_m17
from deep.l7.m21 import value_m21

BASE_25 = 825


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m09(n) + value_m22(n) + value_m02(n) + value_m24(n) + value_m03(n) + value_m16(n) + value_m17(n) + value_m21(n)
