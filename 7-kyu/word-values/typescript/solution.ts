export const wordValue = (arr: string[]): number[] => {
  return arr.map((phrase, idx): number => {
    return (idx + 1) * phrase.replace(/\s/g, "").split("").map(letter => letter.charCodeAt(0) - "a".charCodeAt(0) + 1).reduce((acc, nxt) => acc + nxt, 0);
  });
};
