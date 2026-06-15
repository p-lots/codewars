const newNumeralSystem = number => {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const idx = alphabet.indexOf(number);
  const sums = [];
  for (let i = 0; i < (idx + 1) / 2; i++) {
    const toPush = `${alphabet[i]} + ${alphabet[idx - i]}`;
    sums.push(toPush);
  }
  return sums;
};
