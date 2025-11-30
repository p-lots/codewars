export const multiplicationTable = (size: number): number[][] => {
  return Array.from({ length: size }, (_, i) => {
    const row = Array.from({ length: size }, (_, j) => {
      return (i + 1) * (j + 1);
    });
    return row;
  });
};