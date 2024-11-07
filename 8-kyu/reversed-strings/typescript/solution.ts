export const solution = (str: string): string => {
  const reversed = str
    .split("")
    .reverse()
    .join("");
  return reversed;
}