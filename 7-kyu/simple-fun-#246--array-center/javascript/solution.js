const arrayCenter = a => {
  const min = Math.min(...a);
  const avg = a.reduce((acc, nxt) => acc + nxt, 0) / a.length;
  return a.filter(n => Math.abs(n - avg) < min);
};
