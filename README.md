# arbor-torture

A deliberately adversarial repository for grading
[Arbor](https://getarbor.dev) blast-radius analysis.

Every dependency edge is intentional and documented in
[GROUND_TRUTH.md](GROUND_TRUTH.md), so each pull request has a known correct
answer. That makes it possible to score accuracy rather than eyeball it.

## What it exercises

- A four-level Python call chain with a wide fan-in hub (47 downstream files)
- Dead code that must report **zero** blast radius
- Circular imports that must terminate
- Dynamic and reflective imports that are known to be unresolvable
- Multi-language graphs: Python, JavaScript, TypeScript, Rust, Go
- Parser edge cases: empty files, comments-only, unicode identifiers,
  a 3000-character line, and one deliberately unparseable file

## Not a real project

Nothing here runs in production and nothing here is meant to be useful. The
code exists so a graph can be built over it.
