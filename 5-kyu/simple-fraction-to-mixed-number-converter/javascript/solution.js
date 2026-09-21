const gcd = (x, y) => !y ? x : gcd(y, x % y);

const mixedFraction = s => {
  const [numerator, denominator] = s.split("/").map(Number);
  if (denominator === 0) {
    throw new Error("Division by zero");
  }
  if (numerator === 0) {
    return `${numerator}`;
  }
  const sign = Math.sign(numerator) * Math.sign(denominator);
  const absN = Math.abs(numerator);
  const absD = Math.abs(denominator);
  const greatestCommonDiv = gcd(absN, absD);
  if (absN === absD) {
    return `${sign}`;
  }
  if (absN > absD) {
    if (absN % absD === 0) {
      return `${numerator / denominator}`;
    }
    const remainder = (absN % absD) / greatestCommonDiv;
    const wholePart = Math.floor(absN / absD);
    return `${sign * wholePart} ${remainder}/${absD / greatestCommonDiv}`;
  }
  return `${sign * (absN / greatestCommonDiv)}/${absD / greatestCommonDiv}`;
};
