const sumFactorial = arr => {
  const factorial = num => {
    let result = 1;
    for (let i = 2; i <= num; i++) {
      result *= i;
    }
    return result;
  };
  const total = arr.reduce((acc, nxt) => acc + factorial(nxt), 0);
  return total;
};
