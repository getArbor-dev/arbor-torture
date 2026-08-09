"""Layer 5 module 25. Generated, seed=20260810."""

from deep.l2.m02 import value_m02
from deep.l3.m17 import value_m17
from deep.l3.m18 import value_m18
from deep.l3.m23 import value_m23
from deep.l4.m03 import value_m03
from deep.l4.m14 import value_m14
from deep.l4.m21 import value_m21
from deep.l4.m24 import value_m24

BASE_25 = 525


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m02(n) + value_m17(n) + value_m18(n) + value_m23(n) + value_m03(n) + value_m14(n) + value_m21(n) + value_m24(n)
