const isPrime = n => {
  if (n < 2) {
    return false;
  }
  if (n == 2 || n == 3) {
    return true;
  }
  if (n % 2 === 0 || n % 3 === 0) {
    return false;
  }
  for (let i = 5; i < n; i += 2) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}