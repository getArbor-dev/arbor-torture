"""Layer 9 module 16. Generated, seed=20260810."""

from deep.l6.m00 import value_m00
from deep.l6.m13 import value_m13
from deep.l7.m19 import value_m19
from deep.l8.m01 import value_m01
from deep.l8.m02 import value_m02
from deep.l8.m03 import value_m03
from deep.l8.m08 import value_m08
from deep.l8.m22 import value_m22

BASE_16 = 916


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m00(n) + value_m13(n) + value_m19(n) + value_m01(n) + value_m02(n) + value_m03(n) + value_m08(n) + value_m22(n)
