const alternate = (n, firstValue, secondValue) => {
  const values = [firstValue, secondValue];
  let ret = [];
  for (let i = 0; i < n; i++) {
    ret.push(values[i % values.length]);
  }
  return ret;
};
