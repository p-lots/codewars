const expressionMatter = (a, b, c) => {
  const ret = [a * (b + c), a * b * c, a + b + c, (a + b) * c];
  return Math.max(...ret);
};
