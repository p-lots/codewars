const reduce = (fraction) => {
  const gcd = (a, b) => {
    a = Math.abs(a);
    b = Math.abs(b);
    if (b > a) {
      const temp = a;
      a = b;
      b = temp;
    }
    while (true) {
      if (b === 0) {
        return a;
      }
      a %= b;
      if (a === 0) {
        return b;
      }
      b %= a;
    }
  };
  const [numer, denom] = fraction;
  const hcf = gcd(numer, denom);
  return [numer / hcf, denom / hcf];
};
