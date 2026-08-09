"""Layer 1 module 21. Generated, seed=20260810."""

from deep.l0.m08 import value_m08
from deep.l0.m23 import value_m23

BASE_21 = 121


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m08(n) + value_m23(n)
