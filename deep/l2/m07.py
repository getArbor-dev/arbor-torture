"""Layer 2 module 07. Generated, seed=20260810."""

from deep.l0.m08 import value_m08
from deep.l1.m16 import value_m16

BASE_07 = 207


def value_m07(n: int = 1) -> int:
    # torture: behaviour changed here
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m08(n) + value_m16(n)
