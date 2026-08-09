"""Layer 2 module 20. Generated, seed=20260810."""

from deep.l0.m06 import value_m06
from deep.l0.m25 import value_m25
from deep.l1.m03 import value_m03
from deep.l1.m05 import value_m05
from deep.l1.m10 import value_m10
from deep.l1.m18 import value_m18
from deep.l1.m19 import value_m19
from deep.l1.m23 import value_m23

BASE_20 = 220


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m06(n) + value_m25(n) + value_m03(n) + value_m05(n) + value_m10(n) + value_m18(n) + value_m19(n) + value_m23(n)
