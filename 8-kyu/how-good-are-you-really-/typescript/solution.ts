export const betterThanAverage = (classPoints: number[], yourPoints: number): boolean => {
  const classTotal = classPoints.reduce((acc, nxt) => acc + nxt, 0) + yourPoints;
  const classAvg = classTotal / (classPoints.length + 1);
  return yourPoints > classAvg;
}