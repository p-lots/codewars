Calculator = {
  average: (...nums) => {
    return nums.reduce((acc, nxt) => acc + nxt, 0) / nums.length || 0;
  },
};
