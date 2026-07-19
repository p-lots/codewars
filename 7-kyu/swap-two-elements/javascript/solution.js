const swapTwo = (array, a, b) => {
  const swapped = JSON.parse(JSON.stringify(array));
  const aIdx = array.indexOf(a);
  const bIdx = array.lastIndexOf(b);
  swapped[aIdx] = b;
  swapped[bIdx] = a;
  return swapped;
};
