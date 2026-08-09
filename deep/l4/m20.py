"""Layer 4 module 20. Generated, seed=20260810."""

from deep.l1.m00 import value_m00
from deep.l1.m10 import value_m10
from deep.l1.m19 import value_m19
from deep.l2.m21 import value_m21
from deep.l3.m11 import value_m11
from deep.l3.m12 import value_m12
from deep.l3.m13 import value_m13
from deep.l3.m14 import value_m14

BASE_20 = 420


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m00(n) + value_m10(n) + value_m19(n) + value_m21(n) + value_m11(n) + value_m12(n) + value_m13(n) + value_m14(n)
