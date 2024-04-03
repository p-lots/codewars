const lastDigit = (n, d) => {
  if (d <= 0) {
    return [];
  }
  const nArr = n.toString()
    .split("")
    .slice(-d)
    .map(num => parseInt(num));
  return nArr;
};
