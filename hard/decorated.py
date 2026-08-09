"""Decorators that wrap and rename, obscuring the call edge."""

import functools


def retrying(times: int):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            last = None
            for _ in range(times):
                try:
                    return fn(*a, **kw)
                except ValueError as e:
                    last = e
            raise last
        return wrapper
    return deco


@retrying(3)
def flaky(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    return n * 2


def calls_decorated(n: int) -> int:
    return flaky(n)
