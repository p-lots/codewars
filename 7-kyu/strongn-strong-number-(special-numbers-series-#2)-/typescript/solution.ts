export const strongNumber = (num: number): string => {
  const digits = [...(num.toString())];
  const digitTotal = digits.map(digit => factorial(Number(digit))).reduce((acc, nxt) => acc + nxt, 0);
  return num === digitTotal ? "STRONG!!!!" : "Not Strong !!";
};

const factorial = (n: number): number => {
  if (n === 0) {
    return 1;
  } else if (n <= 2) {
    return n;
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}