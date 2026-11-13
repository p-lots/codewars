export const incrementer = (nums: number[]): number[] => {
  return nums.map((n, idx) => (n + idx + 1) % 10);
};
