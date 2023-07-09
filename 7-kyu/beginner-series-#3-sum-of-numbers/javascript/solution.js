const getSum = (a, b) => {
  const smaller = Math.min(a, b);
  const larger = Math.max(a, b);
  let ret = 0;
  for (let i = smaller; i <= larger; i++) {
    ret += i;
  }
  return ret;
}