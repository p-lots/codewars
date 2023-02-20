const strangeMath = (n, k) => {
  let ret = [];
  for (let i = 0; i <= n; i++) {
    ret.push(`${i}`);
  }
  ret.sort();
  return ret.indexOf(`${k}`);
};