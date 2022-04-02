const sumOfDifferences = (arr) => {
  if (arr.length < 2) return 0;
  let arr2 = arr.sort((a, b) => b - a);
  let ret = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    ret += arr[i] - arr[i + 1];
  }
  return ret;
};