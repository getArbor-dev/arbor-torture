"""Layer 5 module 17. Generated, seed=20260810."""

from deep.l3.m06 import value_m06
from deep.l4.m02 import value_m02
from deep.l4.m04 import value_m04
from deep.l4.m07 import value_m07
from deep.l4.m19 import value_m19
from deep.l4.m21 import value_m21
from deep.l4.m22 import value_m22
from deep.l4.m25 import value_m25

BASE_17 = 517


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m06(n) + value_m02(n) + value_m04(n) + value_m07(n) + value_m19(n) + value_m21(n) + value_m22(n) + value_m25(n)
