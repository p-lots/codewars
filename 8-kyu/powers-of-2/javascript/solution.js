const powersOfTwo = n => {
  let ret = [];
  for (let i = 0; i <= n; i++) {
    ret.push(Math.pow(2, i));
  }
  return ret;
}