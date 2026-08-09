"""Layer 8 module 03. Generated, seed=20260810."""

from deep.l6.m17 import value_m17
from deep.l7.m16 import value_m16

BASE_03 = 803


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m17(n) + value_m16(n)
