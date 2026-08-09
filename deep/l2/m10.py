"""Layer 2 module 10. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m06 import value_m06
from deep.l0.m25 import value_m25
from deep.l1.m19 import value_m19
from deep.l1.m20 import value_m20

BASE_10 = 210


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m00(n) + value_m06(n) + value_m25(n) + value_m19(n) + value_m20(n)
