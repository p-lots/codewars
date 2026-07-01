const gcd = (x, y) => {
  x = Math.abs(x);
  y = Math.abs(y);
  if (y > x) {
    let temp = x;
    x = y;
    y = temp;
  }
  while (true) {
    if (y === 0) {
      return x;
    }
    x %= y;
    if (x === 0) {
      return y;
    }
    y %= x;
  }
};

const finalAttackValue = (x, monsterList) => {
  return monsterList.reduce((curr, nxt) => {
    return nxt > curr ? curr + gcd(nxt, curr) : curr + nxt;
  }, x);
};
