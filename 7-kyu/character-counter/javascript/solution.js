const validateWord = s => {
  const counts = {};
  for (const char of s) {
    if (counts.hasOwnProperty(char.toLowerCase())) {
      counts[char.toLowerCase()] += 1;
    } else {
      counts[char.toLowerCase()] = 1;
    }
  }
  return Object.values(counts).every((elem, idx, arr) => {
    if (idx === 0) {
      return true;
    }
    return elem === arr[idx - 1];
  });
};
