const isPrime = n => {
  if (n < 2) {
    return false;
  }
  if (n === 2 || n === 3) {
    return true;
  }
  if (n % 2 === 0 || n % 3 === 0) {
    return false;
  }
  const limit = Math.floor(Math.sqrt(n)) + 1;
  for (let i = 3; i < limit; i += 2) {
    if (n % i === 0){
      return false;
    }
  }
  return true;
};

const nextPrime = n => {
  if (isPrime(n)) {
    n++;
  }
  while (!isPrime(n)) {
    n++;
  }
  return n;
};
