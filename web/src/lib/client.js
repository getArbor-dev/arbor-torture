import { buildUrl, TIMEOUT_MS } from "./constants.js";

export async function get(path) {
  const res = await fetch(buildUrl(path), { signal: AbortSignal.timeout(TIMEOUT_MS) });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

export async function post(path, body) {
  return fetch(buildUrl(path), { method: "POST", body: JSON.stringify(body) });
}
