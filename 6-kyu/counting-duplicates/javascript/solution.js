const duplicateCount = (text) => {
  text = text.toLowerCase();
  let counts = {};
  for (const ch of text) {
    if (!counts.hasOwnProperty(ch)) {
      counts[ch] = 1;
    } else {
      counts[ch] += 1;
    }
  }
  return Object.entries(counts).filter(elem => elem[1] > 1).length;
};