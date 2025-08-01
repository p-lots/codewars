const ultimateReverse = s => {
  const joined = s.join("");
  const reversed = joined.split("").reverse().join("");
  const lengths = s.map(word => word.length);
  let i = 0;
  const ultimate = [];
  for (const len of lengths) {
    const nextWord = reversed.slice(i, i + len);
    ultimate.push(nextWord);
    i += len;
  }
  return ultimate;
};