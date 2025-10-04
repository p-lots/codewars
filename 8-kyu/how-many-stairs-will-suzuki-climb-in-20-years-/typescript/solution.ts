export const stairsIn20 = (stairs: number[][]): number => {
  const total = stairs.reduce((acc, row) => acc + row.reduce((accum, day) => accum + day, 0), 0);
  return total * 20;
};
