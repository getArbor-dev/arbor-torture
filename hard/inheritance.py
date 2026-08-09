"""Four-level inheritance with overrides at each level.

GROUND TRUTH: a change to Base.compute must reach Leaf, which never
redefines it.
"""


class Base:
    def compute(self, n: int) -> int:
        return n

    def shared(self) -> str:
        return "base"


class Middle(Base):
    def compute(self, n: int) -> int:
        return super().compute(n) * 2


class Derived(Middle):
    def shared(self) -> str:
        return "derived"


class Leaf(Derived):
    """Inherits compute from Middle and shared from Derived."""

    def run(self, n: int) -> int:
        return self.compute(n) + len(self.shared())
