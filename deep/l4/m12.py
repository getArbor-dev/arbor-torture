"""Layer 4 module 12. Generated, seed=20260810."""

from deep.l1.m00 import value_m00
from deep.l1.m09 import value_m09
from deep.l2.m08 import value_m08
from deep.l2.m14 import value_m14
from deep.l3.m02 import value_m02
from deep.l3.m05 import value_m05
from deep.l3.m10 import value_m10
from deep.l3.m23 import value_m23

BASE_12 = 412


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m00(n) + value_m09(n) + value_m08(n) + value_m14(n) + value_m02(n) + value_m05(n) + value_m10(n) + value_m23(n)
