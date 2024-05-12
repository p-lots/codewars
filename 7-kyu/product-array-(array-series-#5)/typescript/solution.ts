export const productArray = (nums: number[]): number[] => {
  const product = nums.reduce((acc, nxt) => acc * nxt, 1);
  const prodArr = [];
  for (let i = 0; i < nums.length; i++) {
    prodArr.push(product / nums[i]);
  }
  return prodArr;
};
