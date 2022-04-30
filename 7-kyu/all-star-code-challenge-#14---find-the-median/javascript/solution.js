const median = array => {
  array = array.sort((a, b) => a - b);
  const mid = Math.floor(array.length / 2);
  return array.length % 2 === 1 ? array[mid] : (array[mid - 1] + array[mid]) / 2;
};
