const battle = (x, y) => {
  const getScore = word => word.split("").map(letter => letter.charCodeAt(0) - 64).reduce((acc, nxt) => acc + nxt, 0);
  return getScore(x) === getScore(y) ? "Tie!" : getScore(x) > getScore(y) ? x : y;
};
