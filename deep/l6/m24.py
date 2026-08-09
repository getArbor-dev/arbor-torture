"""Layer 6 module 24. Generated, seed=20260810."""

from deep.l3.m10 import value_m10
from deep.l3.m16 import value_m16
from deep.l4.m02 import value_m02
from deep.l4.m21 import value_m21
from deep.l5.m00 import value_m00
from deep.l5.m05 import value_m05
from deep.l5.m15 import value_m15
from deep.l5.m19 import value_m19

BASE_24 = 624


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m10(n) + value_m16(n) + value_m02(n) + value_m21(n) + value_m00(n) + value_m05(n) + value_m15(n) + value_m19(n)
