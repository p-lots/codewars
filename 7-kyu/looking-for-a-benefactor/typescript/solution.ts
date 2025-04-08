export const newAvg = (arr: number[], newavg: number): number => {
  const sum = arr.reduce((acc, nxt) => acc + nxt, 0);
  const newMean = Math.ceil(newavg * (arr.length + 1) - sum);
  if (newMean <= 0) {
    throw "Expected New Average is too low";
  }
  return newMean;
}