const nerdify = txt => {
  const replacements = [["a", "4"], ["A", "4"], ["e", "3"], ["E", "3"], ["l", "1"]];
  const lookup = new Map(replacements);
  return [...txt].map(ch => lookup.has(ch) ? lookup.get(ch) : ch).join("");
};
