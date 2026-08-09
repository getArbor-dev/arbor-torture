"""Layer 3 module 08. Generated, seed=20260810."""

from deep.l0.m02 import value_m02
from deep.l1.m18 import value_m18

BASE_08 = 308


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m02(n) + value_m18(n)
