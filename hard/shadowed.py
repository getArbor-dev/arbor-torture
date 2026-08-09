"""Two different symbols with the SAME name in one file's namespace.

GROUND TRUTH: `process` here is NOT the same node as `process` in
hard/shadow_other.py. Conflating them by bare name is a false edge.
"""


def process(data: list) -> int:
    return len(data)


def caller() -> int:
    return process([1, 2, 3])
