const equableTriangle = (a, b, c) => {
  const perimeter = a + b + c;
  const half = perimeter / 2;
  const area = (half * (half - a) * (half - b) * (half - c)) ** 0.5;
  return perimeter === area;
};
