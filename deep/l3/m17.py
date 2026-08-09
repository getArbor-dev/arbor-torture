"""Layer 3 module 17. Generated, seed=20260810."""

from deep.l0.m12 import value_m12
from deep.l0.m18 import value_m18
from deep.l1.m11 import value_m11
from deep.l2.m03 import value_m03
from deep.l2.m04 import value_m04
from deep.l2.m09 import value_m09
from deep.l2.m21 import value_m21
from deep.l2.m25 import value_m25

BASE_17 = 317


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m12(n) + value_m18(n) + value_m11(n) + value_m03(n) + value_m04(n) + value_m09(n) + value_m21(n) + value_m25(n)
