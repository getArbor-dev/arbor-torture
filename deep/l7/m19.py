"""Layer 7 module 19. Generated, seed=20260810."""

from deep.l5.m15 import value_m15
from deep.l6.m00 import value_m00
from deep.l6.m07 import value_m07
from deep.l6.m12 import value_m12
from deep.l6.m23 import value_m23

BASE_19 = 719


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m15(n) + value_m00(n) + value_m07(n) + value_m12(n) + value_m23(n)
