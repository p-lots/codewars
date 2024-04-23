export function noOdds(values: number[]): number[] {
  return values.filter((num) => num % 2 === 0);
}
