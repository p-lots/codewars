const findAverage = (nums) => {
  if (nums.length === 0) {
    return 0;
  }
  return nums.reduce((acc, nxt) => acc + nxt, 0) / nums.length;
};
