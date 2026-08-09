"""A DIFFERENT `process`. Same name, unrelated symbol."""


def process(data: dict) -> int:
    return len(data.keys())


def other_caller() -> int:
    return process({"a": 1})
