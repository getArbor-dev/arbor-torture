# Hard fixture — ground truth

Generated from seed `20260810`. The graph shape is random; the expected answers are
computed from the generator's own edge list, so they are exact rather than
estimated. Full machine-readable copy in `deep/GROUND_TRUTH.json`.

## Random layered DAG

- **260** modules across **10** layers in `deep/`
- **734** import edges, skewed fan-in (most modules take 1-3 deps, some take 8)
- Edges always point to a lower layer, so the graph is acyclic by construction

Downstream counts for a sample of targets:

| Module | Correct downstream |
|---|---|
| `deep.l0.m14` | **179** |
| `deep.l0.m00` | **178** |
| `deep.l0.m07` | **161** |
| `deep.l1.m00` | **143** |
| `deep.l2.m07` | **122** |
| `deep.l1.m14` | **114** |
| `deep.l0.m21` | **100** |
| `deep.l2.m21` | **100** |
| `deep.l2.m14` | **97** |
| `deep.l3.m14` | **96** |
| `deep.l2.m00` | **82** |
| `deep.l1.m21` | **80** |
| `deep.l4.m00` | **61** |
| `deep.l4.m21` | **55** |
| `deep.l3.m21` | **43** |
| `deep.l4.m07` | **43** |
| `deep.l3.m00` | **36** |
| `deep.l3.m07` | **21** |

## Adversarial cases in `hard/`

| File | What it tests | Correct behaviour |
|---|---|---|
| `reexport_leaf.py` | two-hop re-export | change to `reexport_base` **must** reach it |
| `aliased.py` | `import X as Y`, module aliases | edge resolved despite the rename |
| `shadowed.py` / `shadow_other.py` | same symbol name, two files | **two distinct nodes**; merging them is a false edge |
| `conditional.py` | try/except and function-local imports | edges found, no crash |
| `inheritance.py` | 4-level inheritance with overrides | `Base.compute` reaches `Leaf.run` |
| `decorated.py` | `functools.wraps` wrapper | `calls_decorated` reaches `flaky` |
| `deep_chain.py` | 20-deep straight-line chain | `step_00` reaches all 19 above; a depth cap under-reports |
| `self_recursive.py` | direct, mutual, 3-cycle recursion | terminates, no rank inflation |
| `stdlib_shadow.py` | locals named `open`, `len`, `dict` | not confused with builtins |
| `big_file.py` | 800 functions, ~4000 lines | parses within budget |

## Cross-language

Identical 3-layer service in TypeScript, Go and Rust under `poly/`.
Changing each `base`/`core` must reach exactly **2** modules in that language,
and must **not** leak across languages.

## Scoring

A **false positive** — impact reported that the graph does not contain — is the
worst class of error, because it teaches people to ignore the comment. A false
negative is safer but still wrong. Known-unresolvable cases are listed as such
in `GROUND_TRUTH.md` and are not counted against accuracy.
