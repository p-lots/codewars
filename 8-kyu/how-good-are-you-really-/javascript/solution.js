const betterThanAverage = (classPoints, yourPoints) => {
  const classPointsTotal = classPoints.reduce((acc, nxt) => acc + nxt, 0);
  return yourPoints > classPointsTotal / classPoints.length;
};
