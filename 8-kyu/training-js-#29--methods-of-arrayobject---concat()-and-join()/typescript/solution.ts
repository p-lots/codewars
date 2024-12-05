export function bigToSmall(arr: number[][]): string {  
  let flatArr: number[] = [];
  flatArr = flatArr.concat(...arr);
  return flatArr.sort((a, b) => b - a).join(">");
}