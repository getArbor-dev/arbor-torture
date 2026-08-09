"""Layer 7 module 10. Generated, seed=20260810."""

from deep.l4.m00 import value_m00
from deep.l5.m02 import value_m02
from deep.l5.m03 import value_m03
from deep.l5.m18 import value_m18
from deep.l6.m16 import value_m16
from deep.l6.m17 import value_m17
from deep.l6.m21 import value_m21
from deep.l6.m24 import value_m24

BASE_10 = 710


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m00(n) + value_m02(n) + value_m03(n) + value_m18(n) + value_m16(n) + value_m17(n) + value_m21(n) + value_m24(n)
