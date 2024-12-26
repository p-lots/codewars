const circleArea = radius => {
  if (typeof radius !== "number" || radius <= 0) {
    return false;
  }
  return Math.round(radius * radius * Math.PI * 100) / 100;
};
