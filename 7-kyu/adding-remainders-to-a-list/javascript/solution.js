const solve = (nums, div) => {
  return nums.map((number) => number + number % div);
};
