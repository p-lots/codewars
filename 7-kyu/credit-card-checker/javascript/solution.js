const validCard = card => {
  const result = card.replace(/ /g, "")
    .split("")
    .reverse()
    .map(Number)
    .map((digit, idx) => idx % 2 === 1 ? digit * 2 > 9 ? digit * 2 - 9 : digit * 2 : digit)
    .reduce((acc, nxt) => acc + nxt, 0);
  return result % 10 === 0;
};
