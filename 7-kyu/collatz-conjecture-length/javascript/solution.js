const collatz = n => {
  let ret = 1;
  while (n !== 1) {
    n = (n % 2 === 1 ? n * 3 + 1 : Math.floor(n / 2))
    ret++;
  }
  return ret;
};
