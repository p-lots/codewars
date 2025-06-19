export const sortVowels = (str?: number | string | null): string => {
  if (!str || typeof str === "number") {
    return "";
  }
  return str.split("")
    .map(char => "aeiou".includes(char.toLowerCase()) ? `|${char}` : `${char}|`)
    .join("\n");
};
