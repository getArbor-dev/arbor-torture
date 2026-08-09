"""Layer 8 module 11. Generated, seed=20260810."""

from deep.l5.m16 import value_m16
from deep.l5.m18 import value_m18
from deep.l6.m10 import value_m10
from deep.l6.m17 import value_m17
from deep.l7.m02 import value_m02
from deep.l7.m14 import value_m14
from deep.l7.m19 import value_m19
from deep.l7.m25 import value_m25

BASE_11 = 811


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m16(n) + value_m18(n) + value_m10(n) + value_m17(n) + value_m02(n) + value_m14(n) + value_m19(n) + value_m25(n)
