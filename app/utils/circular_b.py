"""Circular import B <-> A."""


def beta(n: int) -> int:
    from app.utils.circular_a import alpha
    if n <= 0:
        return 0
    return alpha(n - 1) + 1
