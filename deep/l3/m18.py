"""Layer 3 module 18. Generated, seed=20260810."""

from deep.l2.m00 import value_m00
from deep.l2.m03 import value_m03
from deep.l2.m04 import value_m04
from deep.l2.m07 import value_m07
from deep.l2.m08 import value_m08
from deep.l2.m14 import value_m14
from deep.l2.m19 import value_m19
from deep.l2.m22 import value_m22

BASE_18 = 318


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m00(n) + value_m03(n) + value_m04(n) + value_m07(n) + value_m08(n) + value_m14(n) + value_m19(n) + value_m22(n)
