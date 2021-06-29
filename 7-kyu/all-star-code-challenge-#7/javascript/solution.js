const compute = n => {
  if (n < 3 || n % 2 === 0) {
    return 0;
  }
  let ret = 0;
  for (let i = 1; i <= n; i += 2) {
    ret += 1 / i ** 2;
  }
  return ret;
}