const SeriesSum = n => {
  let ret = 0;
  for (let i = 0; i < n; i++) {
    ret += 1 / (i * 3 + 1);
  }
  return ret.toFixed(2);
};
