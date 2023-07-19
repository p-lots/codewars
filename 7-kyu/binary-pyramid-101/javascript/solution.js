const binaryPyramid = (m, n) => {
  let ret = [];
  for (let i = m; i <= n; i++) {
    ret.push(parseInt(i.toString(2)));
  }
  return ret.reduce((acc, nxt) => acc + nxt, 0).toString(2);
};
