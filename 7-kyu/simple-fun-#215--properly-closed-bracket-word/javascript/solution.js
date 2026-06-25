const closedBracketWord = word => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const alphaCounterparts = alphabet.split("").reverse().join("");
  const counterpartMap = new Map();
  for (let i = 0; i < alphabet.length; i++) {
    counterpartMap.set(alphabet[i], alphaCounterparts[i]);
  }
  const midpoint = word.length / 2;
  for (let i = 0; i <= midpoint; i++) {
    if (word[i] !== counterpartMap.get(word[word.length - i - 1])) {
      return false;
    }
  }
  return true;
};
