"""Layer 3 module 12. Generated, seed=20260810."""

from deep.l0.m03 import value_m03
from deep.l0.m14 import value_m14
from deep.l0.m25 import value_m25
from deep.l2.m21 import value_m21
from deep.l2.m24 import value_m24

BASE_12 = 312


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m03(n) + value_m14(n) + value_m25(n) + value_m21(n) + value_m24(n)
