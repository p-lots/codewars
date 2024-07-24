const squareArea = A => {
  const result = ((A * 4) / (2 * Math.PI)) ** 2;
  return Math.round(result * 100) / 100;
};
