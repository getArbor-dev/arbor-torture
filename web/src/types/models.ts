export interface User { id: number; login: string; plan: "free" | "pro" | "team"; }
export interface Payment { id: number; amountCents: number; plan: string; }

export type Verdict = "pass" | "review" | "block";

export function isPaid(u: User): boolean {
  return u.plan !== "free";
}
