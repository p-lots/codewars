function mxdiflg(a1, a2) {
  if (a1.length === 0 || a2.length === 0) {
    return -1;
  }
  const a1Sorted = a1.map((elem) => elem.length).sort((a, b) => b - a);
  const a2Sorted = a2.map((elem) => elem.length).sort((a, b) => b - a);
  return Math.max(Math.abs(a1Sorted[a1Sorted.length - 1] - a2Sorted[0]), Math.abs(a2Sorted[a2Sorted.length - 1] - a1Sorted[0]));
};