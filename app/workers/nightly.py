"""Nightly job. GROUND TRUTH: downstream=0."""

from app.services.billing import refund
from app.services.email import send


def run():
    send("ops@example.com", "Nightly", "starting")
    for stale in (101, 102):
        refund(stale)
    send("ops@example.com", "Nightly", "done")
