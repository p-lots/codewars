const battle = (x, y) => {
  const calculateScore = (word) => {
    let ret = 0;
    for (const ch of word) {
      if (ch.toUpperCase() === ch) {
        ret += ch.charCodeAt(0) - "A".charCodeAt(0) + 1;
      } else {
        ret += (ch.charCodeAt(0) - "a".charCodeAt(0) + 1) / 2;
      }
    }
    return ret;
  };
  const xScore = calculateScore(x);
  const yScore = calculateScore(y);
  if (xScore > yScore) {
    return x;
  } else if (xScore === yScore) {
    return "Tie!";
  }
  return y;
};
