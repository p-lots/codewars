function isCoprime(x, y) {
  const bigger = Math.max(x, y);
  for (let i = 2; i <= bigger; i++) {
    if (x % i === 0 && y % i === 0) {
      return false;
    }
  }
  return true;
}