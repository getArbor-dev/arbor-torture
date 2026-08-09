"""Layer 5 module 03. Generated, seed=20260810."""

from deep.l4.m16 import value_m16
from deep.l4.m20 import value_m20
from deep.l4.m23 import value_m23

BASE_03 = 503


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m16(n) + value_m20(n) + value_m23(n)
