"""Circular import A <-> B. Must not infinite-loop the BFS."""


def alpha(n: int) -> int:
    from app.utils.circular_b import beta
    if n <= 0:
        return 0
    return beta(n - 1) + 1
