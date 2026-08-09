"""Layer 1 module 15. Generated, seed=20260810."""

from deep.l0.m08 import value_m08
from deep.l0.m10 import value_m10
from deep.l0.m12 import value_m12
from deep.l0.m13 import value_m13
from deep.l0.m14 import value_m14

BASE_15 = 115


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m08(n) + value_m10(n) + value_m12(n) + value_m13(n) + value_m14(n)
