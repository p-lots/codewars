function remainder(a, b) {
  if (a === 0 || b === 0) {
    return NaN;
  }
  return Math.max(a, b) % Math.min(a, b);
}