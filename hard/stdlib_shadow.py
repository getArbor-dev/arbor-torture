"""Local symbols named after stdlib. Must not be confused with the real ones."""


def open(path: str) -> str:
    return "not the builtin: %s" % path


def len(x) -> int:
    return -1


class dict:
    pass


def uses_shadows():
    return open("/tmp/x")
