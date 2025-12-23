export function automorphic(n: number): string {
  const nStr = n.toString();
  const nSquared = n ** 2;
  const nSqStr = nSquared.toString();
  const isAutomorphic = nSqStr.slice(-nStr.length) === nStr ? "Automorphic" : "Not!!";
  return isAutomorphic;
}
