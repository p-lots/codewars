const swapHeadAndTail = arr => {
  if (arr.length % 2 === 1) {
    const midIdx = Math.floor(arr.length / 2);
    return [...arr.slice(midIdx + 1), arr[midIdx], ...arr.slice(0, midIdx)];
  }
  return [...arr.slice(arr.length / 2), ...arr.slice(0, arr.length / 2)]
};
