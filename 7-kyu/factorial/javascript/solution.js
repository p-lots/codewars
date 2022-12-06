const factorial = n => {
  if (n < 0 || n > 12) {
    throw "RangeError";
  }
  return n === 0 ? 1 : n * factorial(n - 1);
};