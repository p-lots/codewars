const isEven = n => n % 2 === 0;

const divisibleByTen = n => n % 10 === 0;

const isPrime = n => {
  if (n === 2 || n === 3) {
    return true;
  }
  if (n < 2 || n % 2 === 0) {
    return false;
  }
  const limit = Math.trunc(Math.sqrt(n));
  for (let i = 3; i <= limit; i += 2) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

const numberProperty = n => {
  const prime = isPrime(n);
  const even = isEven(n);
  const ten = divisibleByTen(n);
  return [prime, even, ten];
};
