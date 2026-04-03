const box = (n) => {
  if (n === 2) {
    return ["--", "--"];
  }
  const middle = `-${" ".repeat(n - 2)}-`;
  const topAndBottom = "-".repeat(n);
  return [topAndBottom, ...Array(n - 2).fill(middle), topAndBottom];
};
