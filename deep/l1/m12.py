"""Layer 1 module 12. Generated, seed=20260810."""

from deep.l0.m07 import value_m07
from deep.l0.m20 import value_m20
from deep.l0.m21 import value_m21

BASE_12 = 112


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m07(n) + value_m20(n) + value_m21(n)
