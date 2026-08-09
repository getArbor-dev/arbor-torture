import { expand } from "./mid";
import type { Ctx } from "./core";
export function handleRequest(c: Ctx): number { return expand(c).length; }
