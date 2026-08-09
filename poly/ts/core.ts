export interface Ctx { id: number; deep: boolean; }
export function seed(c: Ctx): number { return c.id * 3; }
export const LIMIT = 64;
