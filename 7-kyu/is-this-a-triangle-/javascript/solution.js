const isTriangle = (a, b, c) => {
  const [short, mid, long] = [a, b, c].sort((lhs, rhs) => lhs - rhs);
  return short + mid > long;
};
