"""Layer 1 module 03. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m06 import value_m06
from deep.l0.m07 import value_m07
from deep.l0.m09 import value_m09
from deep.l0.m10 import value_m10

BASE_03 = 103


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m00(n) + value_m06(n) + value_m07(n) + value_m09(n) + value_m10(n)
