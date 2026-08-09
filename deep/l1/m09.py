"""Layer 1 module 09. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m02 import value_m02
from deep.l0.m13 import value_m13
from deep.l0.m18 import value_m18
from deep.l0.m22 import value_m22

BASE_09 = 109


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m00(n) + value_m02(n) + value_m13(n) + value_m18(n) + value_m22(n)
