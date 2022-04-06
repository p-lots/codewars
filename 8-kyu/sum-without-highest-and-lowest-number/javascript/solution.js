const sumArray = (array) => {
  if (!array || array.length <= 1) {
    return 0;
  }
  return array.reduce((acc, curr) => acc + curr, 0) - Math.min(...array) - Math.max(...array);
}