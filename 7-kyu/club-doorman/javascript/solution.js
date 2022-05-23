const passTheDoorMan = word => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  for (let i = 0; i < word.length - 1; i++) {
    if (word[i] == word[i + 1]) {
      return (alphabet.indexOf(word[i]) + 1) * 3;
    }
  }
  return 0;
};