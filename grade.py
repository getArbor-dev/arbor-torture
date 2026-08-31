# -*- coding: utf-8 -*-
"""Grade an Arbor engine run against this fixture's known ground truth.

Usage:
    analyze-local <path-to-arbor-torture> --top 25000 > out.txt
    python grade.py out.txt

Every dependency edge in this repository is deliberate and documented in
GROUND_TRUTH.md and HARD_GROUND_TRUTH.md, so each check below has an exact
expected answer rather than an estimate. Cases listed as known limitations
(dynamic and reflective imports) are excluded on purpose: they are
unresolvable by static analysis and counting them as defects would be dishonest.
"""
import collections
import io
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "out.txt"
txt = io.open(path, encoding="utf-8", errors="replace").read()

ROW = re.compile(
    r"#(\d+)\s+([\d.]+)%\s+(\S+)\s+\S*?([\w\\/.\-]+\.(?:py|js|ts|rs|go))\s+\[(\w+)\]\s+(\d+)\s+callers"
)
rows = [
    {
        "rank": int(m.group(1)),
        "centr": float(m.group(2)),
        "name": m.group(3),
        "file": m.group(4).replace("\\", "/"),
        "kind": m.group(5),
        "callers": int(m.group(6)),
    }
    for m in ROW.finditer(txt)
]
print("  parsed %d symbol rows from %s\n" % (len(rows), path))

by_name = collections.defaultdict(list)
for r in rows:
    by_name[r["name"]].append(r)


def find(name, frag=None):
    for r in by_name.get(name, []):
        if frag is None or frag in r["file"]:
            return r
    return None


PASS, FAIL = [], []


def check(case, ok, detail):
    (PASS if ok else FAIL).append(case)
    print("  %s %-44s %s" % ("ok  " if ok else "FAIL", case, detail))


print("=== A. SYMBOL COLLISION ACROSS MODULES ===")
l0 = find("value_m14", "deep/l0/")
check(
    "deep/l0 value_m14 keeps its own callers",
    bool(l0) and l0["callers"] > 0,
    "callers=%s (0 means its edges went to a sibling)" % (l0["callers"] if l0 else "NOT RANKED"),
)

print("\n=== B. SAME NAME, TWO FILES (must stay two nodes) ===")
sh = find("process", "hard/shadowed.py")
so = find("process", "hard/shadow_other.py")
check("both `process` symbols exist", bool(sh) and bool(so),
      "shadowed=%s other=%s" % (sh["callers"] if sh else "MISSING", so["callers"] if so else "MISSING"))
if sh and so:
    check("neither absorbed the other's call site", sh["callers"] <= 1 and so["callers"] <= 1,
          "callers %s / %s (truth is 1 each)" % (sh["callers"], so["callers"]))

print("\n=== C. BUILTIN SHADOWING ===")
ln = find("len", "hard/stdlib_shadow.py")
check("local `len` does not capture builtin calls",
      bool(ln) and ln["callers"] == 0,
      "callers=%s (truth is 0; it is never called)" % (ln["callers"] if ln else "MISSING"))

print("\n=== D. RE-EXPORT AND ALIAS CHAINS ===")
orig = find("original_function", "hard/reexport_base.py")
check("2-hop re-export and aliases resolve",
      bool(orig) and orig["callers"] >= 4,
      "callers=%s (truth is 4: leaf + 2 aliases + conditional)" % (orig["callers"] if orig else "MISSING"))

print("\n=== E. INHERITANCE EDGES ===")
base = find("Base", "hard/inheritance.py")
check("class Base is reached by its subclasses",
      bool(base) and base["callers"] > 0,
      "callers=%s (truth > 0: Middle extends Base)" % (base["callers"] if base else "MISSING"))

print("\n=== F. CLOSED CYCLE MUST NOT DOMINATE CENTRALITY ===")
ring = [r for r in rows if "evil/ring500.py" in r["file"]]
if ring:
    hi = sum(1 for r in ring if r["centr"] > 90)
    best = min(r["rank"] for r in ring)
    check("500-node ring is not a rank sink", hi < len(ring) * 0.1,
          "%d of %d above 90%%, best rank #%d" % (hi, len(ring), best))

print("\n=== G. DEAD CODE ===")
nc = find("never_called", "app/utils/dead.py")
check("unreachable code is not top-decile",
      bool(nc) and nc["rank"] > len(rows) * 0.10,
      "rank=%s of %s, centrality=%.1f%%" % (nc["rank"], len(rows), nc["centr"]) if nc else "MISSING")

print("\n=== H. DEPTH (20-step chain) ===")
missing = [i for i in range(20) if not find("step_%02d" % i, "hard/deep_chain.py")]
check("all 20 chain steps indexed", not missing, "missing=%s" % (missing or "none"))

print("\n=== I. RISK DISTRIBUTION HAS A MIDDLE ===")
m = re.search(r"Medium \(40-70%\):\s+(\d+) nodes", txt)
lo = re.search(r"Low\s+\(10-40%\):\s+(\d+) nodes", txt)
if m and lo:
    mid = int(m.group(1)) + int(lo.group(1))
    check("scores are not purely bimodal", mid > 0,
          "medium+low = %s nodes (all mass sits at the extremes)" % mid)

print("\n=== J. PARSER ROBUSTNESS ===")
errs = re.search(r"Parse errors:\s+(\d+)", txt)
check("only the deliberately-broken files fail",
      bool(errs) and int(errs.group(1)) <= 2,
      "parse errors=%s (expected 2: broken_syntax.py + binary.py)" % (errs.group(1) if errs else "?"))

print("\n" + "=" * 68)
print("  PASS %d   FAIL %d" % (len(PASS), len(FAIL)))
if FAIL:
    print("  FAILED: " + "; ".join(FAIL))
sys.exit(0)
