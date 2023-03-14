const tArea = tStr => {
  tStr = tStr.trim();
  const count = [...tStr].reduce((acc, next) => acc + (next ==="\n" ? 1 : 0), 0);
  return count * count * 0.5;
}