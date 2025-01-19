export const checkExam = (array1: string[], array2: string[]): number => {
  const score = array1.map((answer: string, idx: number): number => {
    if (answer === array2[idx]) {
      return 4;
    } else if (array2[idx] === "") {
      return 0;
    }
    return -1;
  }).reduce((acc, nxt) => acc + nxt, 0);
  return score < 0 ? 0 : score;
};