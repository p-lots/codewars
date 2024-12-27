export const circleArea = (radius: number): number => {
  if (radius <= 0) {
    throw new Error;
  }
  return Math.PI * radius * radius;
};
