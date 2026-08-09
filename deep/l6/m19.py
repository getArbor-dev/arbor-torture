"""Layer 6 module 19. Generated, seed=20260810."""

from deep.l3.m16 import value_m16
from deep.l4.m22 import value_m22
from deep.l5.m07 import value_m07
from deep.l5.m15 import value_m15
from deep.l5.m25 import value_m25

BASE_19 = 619


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m16(n) + value_m22(n) + value_m07(n) + value_m15(n) + value_m25(n)
