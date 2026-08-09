"""Layer 5 module 19. Generated, seed=20260810."""

from deep.l2.m18 import value_m18
from deep.l4.m23 import value_m23

BASE_19 = 519


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m18(n) + value_m23(n)
