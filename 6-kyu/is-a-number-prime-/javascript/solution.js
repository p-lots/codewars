const isPrime = (num) => {
  if (num < 2) {
    return false;
  } else if (num === 2) {
    return true;
  } else if (num % 2 === 0) {
    return false;
  }
  for (let i = 3; i <= num ** 0.5; i += 2) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}