"""Layer 9 module 03. Generated, seed=20260810."""

from deep.l6.m23 import value_m23
from deep.l8.m16 import value_m16

BASE_03 = 903


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m23(n) + value_m16(n)
