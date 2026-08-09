"""Layer 3 module 03. Generated, seed=20260810."""

from deep.l2.m19 import value_m19
from deep.l2.m24 import value_m24

BASE_03 = 303


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m19(n) + value_m24(n)
