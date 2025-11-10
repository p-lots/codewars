export const sumArray = (array: number[] | null): number => {
  if (array === null || array.length < 2) {
    return 0;
  }
  const lowest = Math.min(...array);
  const highest = Math.max(...array);
  const sum = array.reduce((acc, nxt) => acc + nxt, 0);
  const middleSum = sum - lowest - highest;
  return middleSum;
};
