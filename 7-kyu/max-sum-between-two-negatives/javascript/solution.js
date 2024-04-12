const maxSumBetweenTwoNegatives = (a) => {
  let maxSum = -1;
  let tempSum = 0;
  let negatives = 0;
  for (const num of a) {
    if (num > 0 && negatives > 0) {
      tempSum += num;
    } else if (num < 0) {
      negatives++;
      maxSum = Math.max(tempSum, maxSum);
      tempSum = 0;
    }
  }
  return negatives > 1 ? maxSum : -1;
};
