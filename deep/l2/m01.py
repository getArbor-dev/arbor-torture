"""Layer 2 module 01. Generated, seed=20260810."""

from deep.l0.m11 import value_m11
from deep.l0.m18 import value_m18
from deep.l0.m19 import value_m19
from deep.l0.m25 import value_m25
from deep.l1.m02 import value_m02
from deep.l1.m04 import value_m04
from deep.l1.m14 import value_m14
from deep.l1.m15 import value_m15

BASE_01 = 201


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m11(n) + value_m18(n) + value_m19(n) + value_m25(n) + value_m02(n) + value_m04(n) + value_m14(n) + value_m15(n)
