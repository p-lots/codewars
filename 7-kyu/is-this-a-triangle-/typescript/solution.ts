export const isTriangle = (a: number, b: number, c: number): boolean => {
  const [short, mid, long] = [a, b, c].sort((x, y) => x - y);
  return short + mid > long;
};
