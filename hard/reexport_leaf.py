"""Imports from the re-export, never from the original.

GROUND TRUTH: a change to reexport_base MUST reach here, via reexport_mid.
A graph that only matches direct imports will miss this edge.
"""

from hard.reexport_mid import original_function


def uses_reexported(n: int) -> int:
    return original_function(n) + 1
