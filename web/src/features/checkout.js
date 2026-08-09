import { get, post } from "../lib/client.js";
import { RETRIES } from "../lib/constants.js";

export async function loadPricing() {
  for (let i = 0; i < RETRIES; i++) {
    try { return await get("/pricing"); } catch (e) { if (i === RETRIES - 1) throw e; }
  }
}

export async function submitCheckout(plan) {
  return post("/checkout", { plan });
}
