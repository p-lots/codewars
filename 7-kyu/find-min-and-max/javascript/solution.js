const getMinMax = arr => {
  const smallest = Math.min(...arr);
  const largest = Math.max(...arr);
  return [smallest, largest];
};