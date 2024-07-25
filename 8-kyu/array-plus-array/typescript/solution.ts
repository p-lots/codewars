export const arrayPlusArray = (arr1: number[], arr2: number[]): number => {
  const sum = (array: number[]): number => array.reduce((acc, nxt) => acc + nxt, 0);
  return sum(arr1) + sum(arr2);
};
