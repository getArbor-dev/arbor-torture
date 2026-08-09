import { isPaid, type User, type Verdict } from "../types/models";

const TRIAL_LIMIT = 10;

export function verdictFor(user: User, used: number): Verdict {
  if (isPaid(user)) return "pass";
  if (used < TRIAL_LIMIT) return "review";
  return "block";
}

export function remaining(used: number): number {
  return Math.max(0, TRIAL_LIMIT - used);
}
