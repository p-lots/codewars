const factors = x => {
  if (!Number.isInteger(x) || x < 1) {
    return -1;
  }
  const result = new Set();
  for (let i = 1; i <= Math.floor(Math.sqrt(x)); i++) {
    if (x % i === 0) {
      result.add(i);
      result.add(x / i);
    }
  }
  return Array.from(result).sort((a, b) => b - a);
};
