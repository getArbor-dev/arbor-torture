"""Layer 5 module 14. Generated, seed=20260810."""

from deep.l2.m11 import value_m11
from deep.l2.m12 import value_m12
from deep.l2.m14 import value_m14
from deep.l4.m02 import value_m02
from deep.l4.m19 import value_m19

BASE_14 = 514


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m11(n) + value_m12(n) + value_m14(n) + value_m02(n) + value_m19(n)
