export const binaryArrayToNumber = (arr: number[]): number => {
  const arrJoined = arr.join("");
  const numDecimal = parseInt(arrJoined, 2);
  return numDecimal;
};
