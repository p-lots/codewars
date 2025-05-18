const maxProduct = (numbers, size) => {
  const sorted = numbers.sort((a, b) => b - a);
  const sliced = sorted.slice(0, size);
  return sliced.reduce((acc, nxt) => acc * nxt, 1);
};
