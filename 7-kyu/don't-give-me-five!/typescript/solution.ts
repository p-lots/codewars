export const dontGiveMeFive = (start: number, end: number): number => {
  return Array.from({ length: Math.abs(end - start) + 1 }, (_, idx) => start + idx).filter(n => !(n.toString().includes("5"))).length;
};
