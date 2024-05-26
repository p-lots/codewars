const rangeBitCount = (a, b) => {
  let binArr = [];
  for (let i = a; i <= b; i++) {
    binArr.push(i.toString(2));
  }
  let ret = 0;
  for (const number of binArr) {
    for (const ch of number) {
      if (ch === '1') {
        ret++;
      }
    }
  }
  return ret;
};
