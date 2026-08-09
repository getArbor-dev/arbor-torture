"""Layer 3 module 09. Generated, seed=20260810."""

from deep.l0.m17 import value_m17
from deep.l0.m23 import value_m23
from deep.l2.m07 import value_m07
from deep.l2.m09 import value_m09
from deep.l2.m10 import value_m10
from deep.l2.m19 import value_m19
from deep.l2.m21 import value_m21
from deep.l2.m22 import value_m22

BASE_09 = 309


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m17(n) + value_m23(n) + value_m07(n) + value_m09(n) + value_m10(n) + value_m19(n) + value_m21(n) + value_m22(n)
