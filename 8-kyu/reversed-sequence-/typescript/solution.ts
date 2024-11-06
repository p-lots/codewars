export const reverseSeq = (n: number): number[] => {
  const sequence: number[] = [];
  for (let i = n; i >= 1; i--) {
    sequence.push(i);
  }
  return sequence;
};
