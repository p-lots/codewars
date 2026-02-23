export const divisors = (integer: number): number[] | string => {
  const numbers = Array.from({ length: integer - 1 }, (_, idx) => idx);
  const divs = numbers.filter(n => n > 1 && integer % n === 0);
  return divs.length > 0 ? divs : `${integer} is prime`;
};
