const sumTriangularNumbers = n => {
  let ret = 0;
  for (let i = 1; i <= n; i++) {
    ret += Math.floor(i * (i + 1) / 2);
  }
  return ret;
};
