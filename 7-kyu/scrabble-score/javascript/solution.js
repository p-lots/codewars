const scrabbleScore = str => {
  return str.split("").map(ch => $dict[ch.toUpperCase()] || 0).reduce((acc, nxt) => acc + nxt, 0);
};
