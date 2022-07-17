const generatePairs = (m, n) => {
  let ret = [];
  for (let i = m; i <= n; i++) {
    for (let j = i; j <= n; j++) {
      ret.push([i, j]);
    }
  }
  return ret;
};
