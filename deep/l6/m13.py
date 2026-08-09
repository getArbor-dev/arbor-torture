"""Layer 6 module 13. Generated, seed=20260810."""

from deep.l4.m03 import value_m03
from deep.l4.m24 import value_m24
from deep.l5.m02 import value_m02
from deep.l5.m11 import value_m11
from deep.l5.m14 import value_m14

BASE_13 = 613


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m03(n) + value_m24(n) + value_m02(n) + value_m11(n) + value_m14(n)
