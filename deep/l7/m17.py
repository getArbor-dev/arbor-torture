"""Layer 7 module 17. Generated, seed=20260810."""

from deep.l6.m12 import value_m12
from deep.l6.m18 import value_m18
from deep.l6.m19 import value_m19
from deep.l6.m21 import value_m21
from deep.l6.m25 import value_m25

BASE_17 = 717


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m12(n) + value_m18(n) + value_m19(n) + value_m21(n) + value_m25(n)
