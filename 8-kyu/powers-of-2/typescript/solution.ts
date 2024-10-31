export const powersOfTwo = (n: number): number[] => {
  let powers: number[] = [];
  for (let i = 0; i <= n; i++) {
    powers.push(2 ** i);
  }
  return powers;
}