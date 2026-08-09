"""Layer 8 module 02. Generated, seed=20260810."""

from deep.l5.m19 import value_m19
from deep.l6.m12 import value_m12
from deep.l7.m18 import value_m18
from deep.l7.m20 import value_m20
from deep.l7.m21 import value_m21

BASE_02 = 802


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m19(n) + value_m12(n) + value_m18(n) + value_m20(n) + value_m21(n)
