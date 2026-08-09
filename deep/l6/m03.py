"""Layer 6 module 03. Generated, seed=20260810."""

from deep.l5.m05 import value_m05
from deep.l5.m08 import value_m08

BASE_03 = 603


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m05(n) + value_m08(n)
