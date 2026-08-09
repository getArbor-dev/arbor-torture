"""Layer 3 module 13. Generated, seed=20260810."""

from deep.l0.m23 import value_m23
from deep.l1.m10 import value_m10
from deep.l2.m22 import value_m22

BASE_13 = 313


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m23(n) + value_m10(n) + value_m22(n)
