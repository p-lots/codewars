const countPositivesSumNegatives = input => {
  if (!input || input.length === 0) {
    return [];
  }
  const positives = input.filter(n => n > 0);
  const negatives = input.filter(n => n < 0);
  return [positives.length, negatives.reduce((acc, nxt) => acc + nxt, 0)];
};