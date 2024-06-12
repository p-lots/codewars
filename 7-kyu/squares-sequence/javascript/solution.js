const squares = (x, n) => {
  if (n < 1) {
    return [];
  }
  let ret = [x];
  for (let i = 1; i < n; i++) {
    const squared = ret[ret.length - 1] ** 2;
    ret.push(squared);
  }
  return ret;
};
