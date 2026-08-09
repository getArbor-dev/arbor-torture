// JS hub. GROUND TRUTH: 3 files downstream.
export const API_BASE = "https://api.example.com";
export const TIMEOUT_MS = 8000;
export const RETRIES = 3;

export function buildUrl(path) {
  return `${API_BASE}${path}`;
}
