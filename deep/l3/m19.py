"""Layer 3 module 19. Generated, seed=20260810."""

from deep.l1.m02 import value_m02

BASE_19 = 319


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m02(n)
