const sumCubes = (n) => {
  let ret = 0;
  for (let i = 1; i <= n; i++) {
    ret += i ** 3;
  }
  return ret;
}