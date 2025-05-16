export const isAllPossibilities = (x: number[]): boolean => {
  const xSet = new Set(x);
  for (let i = 0; i < x.length; i++) {
    if (!xSet.has(i)) {
      return false;
    }
  }
  return true;
}