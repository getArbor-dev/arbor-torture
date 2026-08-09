"""Layer 6 module 25. Generated, seed=20260810."""

from deep.l3.m21 import value_m21
from deep.l5.m04 import value_m04
from deep.l5.m05 import value_m05
from deep.l5.m08 import value_m08
from deep.l5.m13 import value_m13

BASE_25 = 625


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m21(n) + value_m04(n) + value_m05(n) + value_m08(n) + value_m13(n)
