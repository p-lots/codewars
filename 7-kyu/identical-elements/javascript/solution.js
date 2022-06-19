const duplicateElements = (m, n) => {
  for (const x of m) {
    for (const y of n) {
      if (x === y) {
        return true;
      }
    }
  }
  return false;
};
     