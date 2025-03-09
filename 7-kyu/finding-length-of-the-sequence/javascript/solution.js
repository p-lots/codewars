const lengthOfSequence = (arr, n) => {
  if (arr.length === 1 && arr.includes(n) || arr.filter(num => num === n).length !== 2) {
    return 0;
  }
  const start = arr.findIndex(num => num === n);
  const end = arr.findLastIndex(num => num === n);
  return end - start + 1;
};
