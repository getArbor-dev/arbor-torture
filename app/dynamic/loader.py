"""Dynamic imports. GROUND TRUTH: these edges are NOT statically resolvable.

Arbor is expected to MISS these. Documented so a miss is scored as a known
limitation rather than counted as a defect, and so that a future improvement
has a fixture to prove itself against.
"""

import importlib

PLUGIN_NAMES = ["app.services.billing", "app.services.email"]


def load_plugin(name: str):
    return importlib.import_module(name)


def load_all():
    return [importlib.import_module(n) for n in PLUGIN_NAMES]


def reflective(module_path: str):
    return __import__(module_path, fromlist=["*"])
