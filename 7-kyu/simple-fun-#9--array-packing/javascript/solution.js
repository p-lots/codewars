const arrayPacking = a => {
  while (a.length < 4) {
    a.push(0);
  }
  a = a.reverse();
  let packed = 0;
  for (let i = 0; i < a.length; i++) {
    const power = 8 * (a.length - i - 1);
    packed += a[i] * Math.pow(2, power);
  }
  return packed;
};
