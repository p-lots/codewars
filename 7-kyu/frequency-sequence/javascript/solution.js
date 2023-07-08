const freqSeq = (str, sep) => {
  let charCounts = {};
  for (const ch of str) {
    if (charCounts[ch]) {
      charCounts[ch] += 1;
    } else {
      charCounts[ch] = 1;
    }
  }
  let ret = [];
  for (const ch of str) {
    ret.push(charCounts[ch].toString());
  }
  return ret.join(sep);
};