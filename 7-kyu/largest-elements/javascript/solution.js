const largest = (n, array) => {
  // Find the n highest elements in a list
  if (n === 0) {
    return [];
  }
  const sorted = array.sort((a, b) => a - b);
  return sorted.slice(-n);
}