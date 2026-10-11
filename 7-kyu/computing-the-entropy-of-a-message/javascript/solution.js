const count = (arr, char) => arr.filter(ch => ch === char).length;

const entropy = message => {
  const noSpaces = [...message].filter(ch => !/\s/.test(ch));
  const totalSymbols = noSpaces.length;
  const uniqueSymbols = new Set(noSpaces);
  let total = 0.0;
  if (totalSymbols === 0 || uniqueSymbols.size < 2) {
    return total;
  }
  for (const sym of uniqueSymbols) {
    const symCount = count(noSpaces, sym);
    total += (symCount / totalSymbols) * Math.log2(symCount / totalSymbols);
  }
  return -total;
};
