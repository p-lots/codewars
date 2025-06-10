const smallestInteger = (matrix) => {
  const flattened = matrix.flat().sort((a, b) => a - b);
  let smallest = 0;
  for (const num of flattened) {
    if (num === smallest) {
      smallest++;
    }
  }
  return smallest;
};
