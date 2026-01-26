const countZeros = (n) => {
  let zeroes = 0;
  for (let i = 1; i <= n; i++) {
    zeroes += `${i}`.replace(/[^0]/g, "").length;
  }
  return zeroes;
};
