const consecutive = (arr, a, b) => {
  const aIndex = arr.indexOf(a);
  const bIndex = arr.indexOf(b);
  return Math.abs(bIndex - aIndex) === 1;
};
