"""Layer 5 module 21. Generated, seed=20260810."""

from deep.l2.m16 import value_m16
from deep.l4.m15 import value_m15
from deep.l4.m19 import value_m19

BASE_21 = 521


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m16(n) + value_m15(n) + value_m19(n)
