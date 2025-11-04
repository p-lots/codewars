export const twoSort = (s: string[]): string => {
  const sorted = s.sort();
  const firstString = sorted[0];
  return firstString.split("").join("***");
};
