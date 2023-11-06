const brightest = colors => {
  const sortByBrightestV = (lhs, rhs) => {
    const lhsCompare = [parseInt(lhs.slice(1, 3), 16), parseInt(lhs.slice(3, 5), 16), parseInt(lhs.slice(5, 7), 16)];
    const rhsCompare = [parseInt(rhs.slice(1, 3), 16), parseInt(rhs.slice(3, 5), 16), parseInt(rhs.slice(5, 7), 16)];
    return Math.max(...rhsCompare) - Math.max(...lhsCompare);
  };
  return colors.sort(sortByBrightestV)[0];
};
