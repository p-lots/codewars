const incrementer = (nums) => {
  return nums.map((elem, idx) => (elem + idx + 1) % 10);
};
