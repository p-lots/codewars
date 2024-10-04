const howMuchILoveYou = (nbPetals) => {
  const phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"];
  let index = nbPetals % phrases.length - 1;
  if (index < 0) {
    index += 6;
  }
  return phrases[index];
};
