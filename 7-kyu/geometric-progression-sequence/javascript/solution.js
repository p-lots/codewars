const geometricSequenceElements = (a, r, n) => {
  const sequence = [a];
  for (let i = 1; i < n; i++) {
    const last = sequence[sequence.length - 1];
    const next = last * r;
    sequence.push(next);
  }
  return sequence.join(", ");
};
