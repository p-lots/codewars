const crap = (x, bags, cap) => {
  let totalCacaCount = 0;
  for (const row of x) {
    if (row.includes("D")) {
      return "Dog!!";
    }
    const rowCacaCount = row.reduce((acc, nxt) => acc + (nxt === "@" ? 1 : 0), 0);
    totalCacaCount += rowCacaCount;
  }
  return bags * cap > totalCacaCount ? "Clean" : "Cr@p";
};
