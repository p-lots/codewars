const solution = (n, b) => {
  let ret = [];
  for (let i = 1; i < 2 ** n; i++) {
    if (i & b) {
      ret.push(i);
    }
  }
  return ret;
};
