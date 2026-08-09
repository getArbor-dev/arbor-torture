"""Layer 2 module 02. Generated, seed=20260810."""

from deep.l0.m04 import value_m04
from deep.l1.m19 import value_m19
from deep.l1.m20 import value_m20

BASE_02 = 202


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m04(n) + value_m19(n) + value_m20(n)
