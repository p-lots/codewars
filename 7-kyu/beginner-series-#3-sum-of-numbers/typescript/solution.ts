export function getSum(a: number, b: number): number {
  let total = 0;
  const smaller = Math.min(a, b);
  const larger = Math.max(a, b);
  for (let i = smaller; i <= larger; i++) {
    total += i;
  }
  return total;
}