export const pipeFix = (numbers: number[]): number[] => {
  const smallest = Math.min(...numbers);
  const largest = Math.max(...numbers);
  const len = largest - smallest + 1;
  return Array.from({ length: len }, (_, idx) => idx + smallest);
}