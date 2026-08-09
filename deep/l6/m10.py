"""Layer 6 module 10. Generated, seed=20260810."""

from deep.l5.m04 import value_m04
from deep.l5.m09 import value_m09
from deep.l5.m13 import value_m13
from deep.l5.m14 import value_m14
from deep.l5.m16 import value_m16
from deep.l5.m18 import value_m18
from deep.l5.m20 import value_m20
from deep.l5.m23 import value_m23

BASE_10 = 610


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m04(n) + value_m09(n) + value_m13(n) + value_m14(n) + value_m16(n) + value_m18(n) + value_m20(n) + value_m23(n)
