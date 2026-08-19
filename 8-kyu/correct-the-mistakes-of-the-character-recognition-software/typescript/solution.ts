export const correct = (s: string): string => {
  const corrections: { [idx: string]: string } = {"5": "S", "0": "O", "1": "I"};
  return [...s].map(ch => corrections[ch] || ch).join("");
};
