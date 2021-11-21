const seven = m => {
  let steps = 0;
  if (m < 1) {
    return [m, steps];
  }
  while (m >= 100) {
    m = Math.floor(m / 10) - (m % 10) * 2;
    steps++;
  }
  return [m, steps];
}