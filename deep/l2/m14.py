"""Layer 2 module 14. Generated, seed=20260810."""

from deep.l1.m05 import value_m05
from deep.l1.m23 import value_m23

BASE_14 = 214


def value_m14(n: int = 1) -> int:
    # torture: behaviour changed here
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m05(n) + value_m23(n)
