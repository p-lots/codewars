export const arr2bin = (arr: any[]): string => {
  const onlyNums = arr.map(elem => typeof elem === 'number' ? elem : 0);
  const binSum = onlyNums.reduce((acc, nxt) => acc + nxt, 0).toString(2);
  return binSum;
};
