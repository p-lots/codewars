const predictAge = (...ages) => {
  const totalSq = ages.reduce((acc, nxt) => acc + nxt * nxt, 0);
  return Math.floor(Math.sqrt(totalSq) / 2);
};
