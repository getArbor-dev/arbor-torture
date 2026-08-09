"""Layer 3 module 00. Generated, seed=20260810."""

from deep.l2.m14 import value_m14
from deep.l2.m19 import value_m19
from deep.l2.m22 import value_m22

BASE_00 = 300


def value_m00(n: int = 1) -> int:
    # torture: behaviour changed here
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m14(n) + value_m19(n) + value_m22(n)
