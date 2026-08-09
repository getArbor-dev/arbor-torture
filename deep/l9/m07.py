"""Layer 9 module 07. Generated, seed=20260810."""

from deep.l6.m00 import value_m00
from deep.l6.m03 import value_m03
from deep.l8.m02 import value_m02
from deep.l8.m06 import value_m06
from deep.l8.m07 import value_m07
from deep.l8.m08 import value_m08
from deep.l8.m14 import value_m14
from deep.l8.m21 import value_m21

BASE_07 = 907


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m00(n) + value_m03(n) + value_m02(n) + value_m06(n) + value_m07(n) + value_m08(n) + value_m14(n) + value_m21(n)
