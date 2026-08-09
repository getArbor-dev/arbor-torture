# Ground truth

Every dependency edge in this repository is deliberate. This file states the
correct answer for each planned change, so Arbor's output can be graded
against arithmetic instead of impressions.

## Python graph

```
config ──▶ db ──▶ auth ──▶ billing ──▶ routes
   │        │       │         │  │        ▲
   │        └───────┴─────────┘  ├─▶ admin│
   └──▶ email ─────────────────────┴──────┘
             └──▶ nightly ◀── billing
```

Plus 40 generated modules in `app/generated/` that each import `config`.

| Change | Correct downstream set | Count |
|---|---|---|
| `core/config.py` | db, email, auth, billing, routes, admin, nightly + 40 generated | **47** |
| `core/logger.py` | db, auth, billing, email, routes, admin, nightly | **7** |
| `core/db.py` | auth, billing, routes, admin, nightly | **5** |
| `services/auth.py` | billing, routes, admin, nightly | **4** |
| `services/billing.py` | routes, admin, nightly | **3** |
| `services/email.py` | routes, nightly | **2** |
| `api/routes.py` | nothing | **0** |
| `api/admin.py` | nothing | **0** |
| `workers/nightly.py` | nothing | **0** |
| **`utils/dead.py`** | **nothing — any hit is a FALSE POSITIVE** | **0** |

## Known limitations — expected misses, not defects

| Case | File | Expectation |
|---|---|---|
| Dynamic `importlib` | `app/dynamic/loader.py` | edges to billing/email NOT resolved |
| Reflective `__import__` | `app/dynamic/loader.py` | not resolved |
| Dynamic `import()` | `web/src/features/dynamic.js` | not resolved |
| `eval(require(...))` | `web/src/features/dynamic.js` | not resolved |
| Circular imports | `app/utils/circular_{a,b}.py` | must terminate, must not hang |

## Parser robustness

| File | Expectation |
|---|---|
| `app/edge/empty.py` | parses, zero symbols, no crash |
| `app/edge/comments_only.py` | parses, zero symbols, no crash |
| `app/edge/unicode_ident.py` | Spanish + Chinese identifiers, emoji, 3000-char line |
| `app/edge/broken_syntax.py` | unparseable; must degrade, not crash the run |

## Other languages

| Change | Correct downstream | Count |
|---|---|---|
| `web/src/lib/constants.js` | client, checkout | **2** |
| `web/src/types/models.ts` | entitlement | **1** |
| `rust/src/config.rs` | engine, report | **2** |
| `go/config/config.go` | worker | **1** |

## Scoring

- **False positive** — Arbor reports impact that the graph does not contain.
  Worst class of error: it trains people to ignore the comment.
- **False negative** — Arbor misses a real edge. Bad, but safer.
- **Known miss** — listed above. Not counted against accuracy; tracked so an
  improvement has something to prove itself against.
