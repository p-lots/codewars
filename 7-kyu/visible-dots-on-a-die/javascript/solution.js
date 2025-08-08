const totalAmountVisible = (topNum, numOfSides) => {
  const totalDots = Math.floor(numOfSides * (numOfSides + 1) / 2);
  const oppositeDots = numOfSides + 1 - topNum;
  return totalDots - oppositeDots;
};
