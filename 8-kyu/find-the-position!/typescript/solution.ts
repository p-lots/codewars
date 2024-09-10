export const position = (alphabet: string): string => {
  const aCharCode = "a".charCodeAt(0);
  const alphaPos = alphabet.charCodeAt(0) - aCharCode + 1;
  return `Position of alphabet: ${alphaPos}`;
}