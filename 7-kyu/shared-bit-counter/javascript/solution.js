const sharedBits = (a, b) => {
  let larger = Math.max(a, b);
  let smaller = Math.min(a, b);
  let total = 0;
  while (smaller > 0 && larger > 0) {
    total += (larger & 1) & (smaller & 1);
    larger >>= 1;
    smaller >>= 1;
  }
  return total > 1;
};
