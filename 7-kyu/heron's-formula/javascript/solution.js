const heron = (a, b, c) => {
  const s = (a + b + c) / 2;
  return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)), 2);
};
