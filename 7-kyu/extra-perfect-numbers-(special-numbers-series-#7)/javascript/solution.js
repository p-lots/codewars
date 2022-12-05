const extraPerfect = n => {
  let ret = [];
  for (let i = 1; i <= n; i += 2) {
    ret.push(i);
  }
  return ret;
}