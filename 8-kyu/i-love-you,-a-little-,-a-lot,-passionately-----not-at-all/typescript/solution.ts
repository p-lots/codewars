export const howMuchILoveYou = (petals: number): string => {
  const phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"];
  return phrases[(petals - 1) % phrases.length];
};
