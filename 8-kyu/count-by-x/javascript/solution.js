const countBy = (x, n) => {
  let ret = [];
  for (let i = 1; i <= n; i++) {
    ret.push(x * i);
  }
  return ret;
}