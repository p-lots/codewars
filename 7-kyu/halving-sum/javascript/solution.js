const halvingSum = n => {
  let ret = n;
  let next = Math.floor(n / 2);
  while (next > 0) {
    ret += next;
    next = Math.floor(next / 2);
  }
  return ret;
};
