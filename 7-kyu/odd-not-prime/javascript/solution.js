const isPrime = n => {
  if (n < 2 && n > 0) {
    return false;
  }
  if (n === 2 || n === 3) {
    return true;
  }
  if (n % 2 === 0 || n % 3 === 0) {
    return false;
  }
  const limit = Math.floor(Math.sqrt(n));
  for (let i = 3; i <= limit; i += 2) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

const oddNotPrime = (n) => {
  return Array(n).fill(1)
    .map((number, idx) => number + idx)
    .filter(number => number % 2 !== 0 && !isPrime(number))
    .length;
}