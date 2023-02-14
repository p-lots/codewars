const gps = (s, x) => {
  if (x.length === 0) {
    return 0;
  }
  let ret = [];
  for (let i = 0; i < x.length - 1; i++) {
    ret.push(3600 * Math.max(x[i + 1] - x[i], 0) / s);
  }
  return ret.length > 0 ? Math.round(Math.max(...ret)) : 0;
};
