"""DEAD CODE. GROUND TRUTH: blast radius MUST be 0.

Nothing in this repository imports this module. If Arbor reports any
downstream impact for a change here, that is a FALSE POSITIVE.
"""


def never_called(x: int) -> int:
    return x * 2


def also_never_called() -> str:
    return "unreachable"


class OrphanClass:
    def method(self):
        return never_called(21)
