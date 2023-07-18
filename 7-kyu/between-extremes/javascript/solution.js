const betweenExtremes = numbers => {
  const largest = Math.max(...numbers);
  const smallest = Math.min(...numbers);
  return largest - smallest;
};
