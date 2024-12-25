const isAnagram = (test, original) => {
  const testLower = test.toLowerCase();
  const origLower = original.toLowerCase();
  const testCounts = {};
  const origCounts = {};
  for (const letter of testLower) {
    testCounts[letter] = testCounts[letter] + 1 || 1;
  }
  for (const letter of origLower) {
    origCounts[letter] = origCounts[letter] + 1 || 1;
  }
  if (Object.entries(origCounts).length !== Object.entries(testCounts).length) {
    return false;
  }
  for (const [ letter, count ] of Object.entries(origCounts)) {
    if (count !== testCounts[letter]) {
      return false;
    }
  }
  return true;
};
