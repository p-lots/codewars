const distancesFromAverage = (arr) => {
  const avg = arr.reduce((acc, nxt) => acc + nxt, 0) / arr.length;
  return arr.map(n => Math.round((avg - n) * 100) / 100);
};
