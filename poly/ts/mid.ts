import { seed, LIMIT, type Ctx } from "./core";
export function expand(c: Ctx): number[] {
  return Array.from({ length: Math.min(seed(c), LIMIT) }, (_, i) => i);
}
