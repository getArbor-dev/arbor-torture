"""Layer 1 module 19. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m02 import value_m02
from deep.l0.m05 import value_m05
from deep.l0.m06 import value_m06
from deep.l0.m13 import value_m13
from deep.l0.m14 import value_m14
from deep.l0.m15 import value_m15
from deep.l0.m25 import value_m25

BASE_19 = 119


def value_m19(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_19 * n + value_m00(n) + value_m02(n) + value_m05(n) + value_m06(n) + value_m13(n) + value_m14(n) + value_m15(n) + value_m25(n)
