const wordPattern = word => {
  const seenLetters = new Map();
  let curr = 0;
  const pattern = [];
  for (const letter of word.toLowerCase()) {
    if (!seenLetters.has(letter)) {
      seenLetters.set(letter, curr);
      curr++;
    }
    const currLetter = seenLetters.get(letter);
    pattern.push(currLetter);
  }
  return pattern.map(letter => letter.toString()).join(".")
};
