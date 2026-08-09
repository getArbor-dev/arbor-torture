"""Layer 2 module 19. Generated, seed=20260810."""

from deep.l0.m09 import value_m09
from deep.l1.m02 import value_m02
from deep.l1.m03 import value_m03

BASE_19 = 219


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m09(n) + value_m02(n) + value_m03(n)
