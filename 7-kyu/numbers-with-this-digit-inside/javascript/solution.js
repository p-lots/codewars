const numbersWithDigitInside = (x, d) => {
  let foundNums = [];
  for (let i = 1; i <= x; i++) {
    if (i.toString().includes(d.toString())) {
      foundNums.push(i);
    }
  }
  const total = foundNums.reduce((acc, nxt) => acc + nxt, 0);
  const product = foundNums.length > 0 ? foundNums.reduce((acc, nxt) => acc * nxt, 1) : 0;
  return [foundNums.length, total, product];
};
