"""Layer 4 module 02. Generated, seed=20260810."""

from deep.l3.m04 import value_m04
from deep.l3.m08 import value_m08
from deep.l3.m16 import value_m16
from deep.l3.m18 import value_m18
from deep.l3.m20 import value_m20

BASE_02 = 402


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m04(n) + value_m08(n) + value_m16(n) + value_m18(n) + value_m20(n)
