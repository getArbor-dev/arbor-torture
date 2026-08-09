// Dynamic import — GROUND TRUTH: not statically resolvable, expected MISS.
export async function loadFeature(name) {
  const mod = await import(`./${name}.js`);
  return mod.default;
}

export function requireish(name) {
  // eslint-disable-next-line
  return eval(`require("./${name}.js")`);
}
