"""A 20-deep straight-line call chain in ONE file.

GROUND TRUTH: changing step_00 reaches all 19 above it. Tests BFS depth
limits — anything that caps at 8 or 10 will under-report.
"""

def step_00(n: int) -> int:
    return n

def step_01(n: int) -> int:
    return step_00(n) + 1

def step_02(n: int) -> int:
    return step_01(n) + 1

def step_03(n: int) -> int:
    return step_02(n) + 1

def step_04(n: int) -> int:
    return step_03(n) + 1

def step_05(n: int) -> int:
    return step_04(n) + 1

def step_06(n: int) -> int:
    return step_05(n) + 1

def step_07(n: int) -> int:
    return step_06(n) + 1

def step_08(n: int) -> int:
    return step_07(n) + 1

def step_09(n: int) -> int:
    return step_08(n) + 1

def step_10(n: int) -> int:
    return step_09(n) + 1

def step_11(n: int) -> int:
    return step_10(n) + 1

def step_12(n: int) -> int:
    return step_11(n) + 1

def step_13(n: int) -> int:
    return step_12(n) + 1

def step_14(n: int) -> int:
    return step_13(n) + 1

def step_15(n: int) -> int:
    return step_14(n) + 1

def step_16(n: int) -> int:
    return step_15(n) + 1

def step_17(n: int) -> int:
    return step_16(n) + 1

def step_18(n: int) -> int:
    return step_17(n) + 1

def step_19(n: int) -> int:
    return step_18(n) + 1


def entry_deep(n: int) -> int:
    return step_19(n)
