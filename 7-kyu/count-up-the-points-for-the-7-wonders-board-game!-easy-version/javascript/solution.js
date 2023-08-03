const solve = (compasses, gears, tablets) => {
  const cards = [compasses, gears, tablets];
  const points = Math.min(...cards) * 7 + cards.reduce((acc, nxt) => acc + nxt * nxt, 0);
  return points;
};
