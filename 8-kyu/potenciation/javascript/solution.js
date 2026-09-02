const power = (x, y) => {
  if ((x === 0 && y === 0) || x === 1) {
    return 1;
  } else if (x === 0) {
    return 0;
  } else if (x < 1 || y < 1) {
    return 1;
  }
  let start = BigInt(x);
  let bigX = BigInt(x);
  for (let i = 1; i < y; i++) {
    start *= bigX;
  }
  return Number(start);
};
