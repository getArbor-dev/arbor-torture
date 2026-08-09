"""Layer 8 module 19. Generated, seed=20260810."""

from deep.l5.m09 import value_m09
from deep.l7.m10 import value_m10
from deep.l7.m25 import value_m25

BASE_19 = 819


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m09(n) + value_m10(n) + value_m25(n)
