export const squareSum = (numbers: number[]): number => {
  return numbers.reduce((acc, nxt) => acc + nxt * nxt, 0);
};
