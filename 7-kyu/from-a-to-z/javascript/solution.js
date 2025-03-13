const gimmeTheLetters = (sp) => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const spSplit = sp.split("-");
  const startLetter = spSplit[0].toLowerCase();
  const endLetter = spSplit[1].toLowerCase();
  const startIdx = alphabet.indexOf(startLetter);
  const endIdx = alphabet.indexOf(endLetter);
  const range = alphabet.slice(startIdx, endIdx + 1);
  if (sp[0].toUpperCase() === sp[0]) {
    return range.toUpperCase();
  }
  return range;
};
