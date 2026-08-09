"""Layer 2 module 03. Generated, seed=20260810."""

from deep.l0.m06 import value_m06
from deep.l0.m25 import value_m25
from deep.l1.m08 import value_m08
from deep.l1.m12 import value_m12
from deep.l1.m18 import value_m18

BASE_03 = 203


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m06(n) + value_m25(n) + value_m08(n) + value_m12(n) + value_m18(n)
