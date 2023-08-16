const secondSymbol = (s, symbol) => {
  const firstIdx = s.indexOf(symbol);
  const nextIdx = s.indexOf(symbol, firstIdx + 1);
  return nextIdx;
};
