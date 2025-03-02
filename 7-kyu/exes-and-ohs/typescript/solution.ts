export const xo = (str: string): boolean => {
  const xCount = str.split("").filter((ch) => ch.toLowerCase() === "x").length;
  const oCount = str.split("").filter((ch) => ch.toLowerCase() === "o").length;
  return xCount === oCount;
};
