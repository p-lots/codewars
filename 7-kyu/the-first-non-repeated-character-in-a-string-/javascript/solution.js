const firstNonRepeated = s => {
  let charCounts = {};
  for (let i = 0; i < s.length; i++) {
    if (!charCounts.hasOwnProperty(s[i])) {
      charCounts[s[i]] = 1;
    } else {
      charCounts[s[i]] += 1;
    }
  }
  for (let i = 0; i < s.length; i++) {
    if (charCounts[s[i]] === 1) {
      return s[i];
    } 
  }
  return null;
};
