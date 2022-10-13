// return the missing number!
const findNumber = array => {
  const currentSum = array.reduce((acc, nxt) => acc + nxt, 0);
  const expectedSum = Math.floor((array.length + 1) * (array.length + 2) / 2);
  return expectedSum - currentSum;
};
