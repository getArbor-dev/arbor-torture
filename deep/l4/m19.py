"""Layer 4 module 19. Generated, seed=20260810."""

from deep.l3.m07 import value_m07

BASE_19 = 419


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m07(n)
