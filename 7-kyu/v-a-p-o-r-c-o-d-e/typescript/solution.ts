export const vaporcode = (str: string): string => {
  return str.replace(/ /g, "")
    .split("")
    .map(ch => ch.toUpperCase())
    .join("  ");
};
