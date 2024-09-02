export const fakeBin = (x: string): string => x.split("")
  .map(digit => parseInt(digit) < 5 ? "0" : "1")
  .join("");
