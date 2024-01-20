const bingo = (a) => {
  const winningPhrase = "BINGO";
  const winningNumbers = [...winningPhrase].map((elem) => elem.charCodeAt(0) - "A".charCodeAt(0) + 1);
  return winningNumbers.every((elem) => a.includes(elem)) ? "WIN" : "LOSE";
};
