export const solve = (s: string): number => {
  const numbers = s.split(/[a-z]*[^\d]/gi);
  const mapped = numbers.map(Number);
  return Math.max(...mapped);
};
