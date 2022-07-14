const consecutiveOnes = nums => {
  let currOneCount = 0;
  let max = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      currOneCount++;
    } else {
      currOneCount = 0;
    }
    if (currOneCount > max) {
      max = currOneCount;
    }
  }
  return max;
};
