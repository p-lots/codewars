const mygcd = (x, y) => {
  while (true) {
    if (x === 0) return y;
    y %= x;
    if (y === 0) return x;
    x %= y;
  }
}