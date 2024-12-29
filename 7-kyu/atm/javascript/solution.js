const solve = n => {
  if (n % 10 !== 0) {
    return -1;
  }
  const denoms = [500, 200, 100, 50, 20, 10];
  let count = 0;
  for (const denom of denoms) {
    while (n >= denom) {
      n -= denom;
      count++;
    }
  }
  return count;
};
