"""Imports inside try/except and inside functions."""

try:
    from hard.reexport_base import original_function
    HAVE_IT = True
except ImportError:
    original_function = None
    HAVE_IT = False


def maybe(n: int) -> int:
    if not HAVE_IT:
        return 0
    return original_function(n)


def function_local_import(n: int) -> int:
    from hard.shadowed import process
    return process([0] * n)
