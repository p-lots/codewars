export function divCon(x: (string | number)[]): number {
  let numsSum = 0;
  let strsSum = 0;
  for (const elem of x) {
    if (typeof elem === 'string') {
      strsSum += Number(elem);
    } else {
      numsSum += elem;
    }
  }
  return numsSum - strsSum;
}