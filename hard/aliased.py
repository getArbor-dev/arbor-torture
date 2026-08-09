"""Aliased imports. The local name never matches the definition."""

from hard.reexport_base import original_function as renamed
import hard.reexport_base as base_mod


def via_alias(n: int) -> int:
    return renamed(n)


def via_module_alias(n: int) -> int:
    return base_mod.original_function(n)
