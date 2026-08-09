"""Admin routes. GROUND TRUTH: downstream=0."""

from app.services.billing import refund, PRO_CENTS


def handle_refund(payment_id: int):
    ok = refund(payment_id)
    return {"status": 200 if ok else 500}


def handle_stats():
    return {"pro_price_cents": PRO_CENTS}
