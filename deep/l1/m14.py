"""Layer 1 module 14. Generated, seed=20260810."""

from deep.l0.m09 import value_m09
from deep.l0.m25 import value_m25

BASE_14 = 114


def value_m14(n: int = 1) -> int:
    # torture: behaviour changed here
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m09(n) + value_m25(n)
