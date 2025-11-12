export const rentalCarCost = (d: number): number => {
  const total = d * 40;
  if (d >= 7) {
    return total - 50;
  } else if (d >= 3) {
    return total - 20;
  }
  return total;
};
