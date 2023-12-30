const sumOfN = (n) => {
  let ret = [];
  for (let i = 0; i <= Math.abs(n); i++) {
    let sum = Math.floor(i * (i + 1) / 2) * (n < 0 && i > 0 ? -1 : 1);
    ret.push(sum);
  }
  return ret;
};
