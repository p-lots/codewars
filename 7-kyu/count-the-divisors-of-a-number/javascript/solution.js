const getDivisorsCnt = n => {
  let ret = 0;
  for (let i = 0; i <= n; i++) {
    if (n % i === 0) {
      ret++;
    }
  }
  return ret;
};