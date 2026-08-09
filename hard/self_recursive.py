"""Direct and mutual recursion. Must terminate the walk."""


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def even(n: int) -> bool:
    return True if n == 0 else odd(n - 1)


def odd(n: int) -> bool:
    return False if n == 0 else even(n - 1)


def triple_a(n): return triple_b(n - 1) if n > 0 else 0
def triple_b(n): return triple_c(n - 1) if n > 0 else 0
def triple_c(n): return triple_a(n - 1) if n > 0 else 0
