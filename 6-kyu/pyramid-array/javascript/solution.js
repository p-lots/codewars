const pyramid = n => {
  let ret = [];
  for (let i = 1; i <= n; i++) {
    let inner = [];
    for (let j = 1; j <= i; j++) {
      inner.push(1);
    }
    ret.push(inner);
  }
  return ret;
};